#!/usr/bin/env python3
"""Build an XMind file from structured functional test cases."""

from __future__ import annotations

import argparse
import json
import shutil
import tempfile
import uuid
import zipfile
from pathlib import Path
from typing import Any, Dict, List

ALLOWED_PRIORITIES = {"P0", "P1", "P2", "P3"}


def _topic(title: str, children: List[Dict[str, Any]] | None = None) -> Dict[str, Any]:
    node: Dict[str, Any] = {
        "id": str(uuid.uuid4()),
        "class": "topic",
        "title": title,
    }
    if children:
        node["children"] = {"attached": children}
    return node


def _list_field_topic(name: str, items: List[str]) -> Dict[str, Any]:
    child_topics = [_topic(f"{idx}. {item}") for idx, item in enumerate(items, start=1)]
    return _topic(name, child_topics)


def _validate_string(value: Any, path: str) -> str:
    if not isinstance(value, str):
        raise ValueError(f"Invalid input at {path}: expected string")
    text = value.strip()
    if not text:
        raise ValueError(f"Invalid input at {path}: string cannot be empty")
    return text


def _validate_string_list(value: Any, path: str) -> List[str]:
    if not isinstance(value, list):
        raise ValueError(f"Invalid input at {path}: expected array")
    if not value:
        raise ValueError(f"Invalid input at {path}: array cannot be empty")

    result: List[str] = []
    for idx, item in enumerate(value):
        result.append(_validate_string(item, f"{path}[{idx}]"))
    return result


def load_cases(input_path: Path) -> Dict[str, Any]:
    try:
        raw = json.loads(input_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in {input_path}: {exc}") from exc

    if not isinstance(raw, dict):
        raise ValueError("Invalid input at $: expected object")

    modules = raw.get("modules")
    if not isinstance(modules, list):
        raise ValueError("Invalid input at modules: expected array")
    if not modules:
        raise ValueError("Invalid input at modules: array cannot be empty")

    normalized_modules: List[Dict[str, Any]] = []
    for mod_idx, module in enumerate(modules):
        mod_path = f"modules[{mod_idx}]"
        if not isinstance(module, dict):
            raise ValueError(f"Invalid input at {mod_path}: expected object")

        module_name = _validate_string(module.get("name"), f"{mod_path}.name")
        cases = module.get("cases")
        if not isinstance(cases, list):
            raise ValueError(f"Invalid input at {mod_path}.cases: expected array")
        if not cases:
            raise ValueError(f"Invalid input at {mod_path}.cases: array cannot be empty")

        normalized_cases: List[Dict[str, Any]] = []
        for case_idx, case in enumerate(cases):
            case_path = f"{mod_path}.cases[{case_idx}]"
            if not isinstance(case, dict):
                raise ValueError(f"Invalid input at {case_path}: expected object")

            title = _validate_string(case.get("title"), f"{case_path}.title")
            priority = _validate_string(case.get("priority"), f"{case_path}.priority").upper()
            if priority not in ALLOWED_PRIORITIES:
                allowed = ", ".join(sorted(ALLOWED_PRIORITIES))
                raise ValueError(
                    f"Invalid input at {case_path}.priority: expected one of {allowed}"
                )

            preconditions = _validate_string_list(
                case.get("preconditions"), f"{case_path}.preconditions"
            )
            steps = _validate_string_list(case.get("steps"), f"{case_path}.steps")
            expected = _validate_string_list(
                case.get("expected_results"), f"{case_path}.expected_results"
            )

            normalized_cases.append(
                {
                    "title": title,
                    "priority": priority,
                    "preconditions": preconditions,
                    "steps": steps,
                    "expected_results": expected,
                }
            )

        normalized_modules.append({"name": module_name, "cases": normalized_cases})

    return {"modules": normalized_modules}


def build_root_topic(root_title: str, modules: List[Dict[str, Any]]) -> Dict[str, Any]:
    module_topics: List[Dict[str, Any]] = []

    for module in modules:
        case_topics: List[Dict[str, Any]] = []
        for case in module["cases"]:
            case_fields = [
                _topic(f"模块: {module['name']}"),
                _topic(f"优先级: {case['priority']}"),
                _list_field_topic("前置条件", case["preconditions"]),
                _list_field_topic("执行步骤", case["steps"]),
                _list_field_topic("预期结果", case["expected_results"]),
            ]
            case_topics.append(_topic(case["title"], case_fields))

        module_topics.append(_topic(module["name"], case_topics))

    return {
        "id": str(uuid.uuid4()),
        "class": "topic",
        "title": root_title,
        "children": {"attached": module_topics},
    }


def write_xmind(
    template_path: Path,
    output_path: Path,
    root_title: str,
    modules: List[Dict[str, Any]],
) -> None:
    if not template_path.exists():
        raise FileNotFoundError(f"Template not found: {template_path}")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="autocase_xmind_") as tmp_dir:
        tmp_path = Path(tmp_dir)
        with zipfile.ZipFile(template_path, "r") as zin:
            zin.extractall(tmp_path)

        content_file = tmp_path / "content.json"
        if not content_file.exists():
            raise FileNotFoundError(
                "Template is invalid: content.json is missing in the .xmind archive"
            )

        data = json.loads(content_file.read_text(encoding="utf-8"))
        if not isinstance(data, list) or not data:
            raise ValueError("Template is invalid: content.json must be a non-empty array")

        sheet = data[0]
        if not isinstance(sheet, dict):
            raise ValueError("Template is invalid: first sheet entry must be an object")

        original_root = sheet.get("rootTopic")
        if not isinstance(original_root, dict):
            raise ValueError("Template is invalid: rootTopic missing in first sheet")

        new_root = build_root_topic(root_title=root_title, modules=modules)

        # Keep template layout behavior to preserve visual style compatibility.
        for key in ("structureClass", "extensions"):
            if key in original_root:
                new_root[key] = original_root[key]

        sheet["rootTopic"] = new_root

        content_file.write_text(
            json.dumps(data, ensure_ascii=False, separators=(",", ":")),
            encoding="utf-8",
        )

        # Repack as a valid .xmind (zip) file.
        with zipfile.ZipFile(output_path, "w", compression=zipfile.ZIP_DEFLATED) as zout:
            for path in sorted(tmp_path.rglob("*")):
                if path.is_file():
                    arcname = str(path.relative_to(tmp_path))
                    zout.write(path, arcname)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate XMind functional test cases from structured JSON input"
    )
    parser.add_argument("--template", required=True, help="Path to the template .xmind file")
    parser.add_argument("--input", required=True, help="Path to input cases JSON file")
    parser.add_argument("--output", required=True, help="Path to output .xmind file")
    parser.add_argument(
        "--root-title",
        default="功能测试用例",
        help="Root topic title (default: 功能测试用例)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    template = Path(args.template).expanduser().resolve()
    input_path = Path(args.input).expanduser().resolve()
    output_path = Path(args.output).expanduser().resolve()

    if not input_path.exists():
        raise FileNotFoundError(f"Input JSON not found: {input_path}")

    payload = load_cases(input_path)
    write_xmind(
        template_path=template,
        output_path=output_path,
        root_title=args.root_title,
        modules=payload["modules"],
    )

    print(f"Generated XMind: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
