---
name: "case-writer"
description: "Generate detailed functional test cases from requirement docs or prototypes using XMind template. Invoke when user asks to create test cases, generate test cases, or write test cases from requirements/prototypes."
---

# Case Writer

Generate detailed functional test cases from requirement documents or prototype images, output as XMind file.

## Template

Use the template file: `/Users/ivi/Dev/xmind/模板-登录注册.xmind`

## Workflow

1. **Parse Input**: Read requirement document or prototype image to extract modules and feature points.
2. **Generate Cases**: Create test cases with standard coverage:
   - 1 normal path case
   - 1 key abnormal case (invalid input or wrong state)
   - 1 key boundary case (empty/length/count/time-window)
3. **Build JSON**: Create structured JSON with case ID format `TC001`, `TC002`, etc.
4. **Run Script**: Execute `autocase/scripts/build_xmind_from_cases.py` to generate XMind.
5. **Return Output**: Provide the generated `.xmind` file path.

## Case ID Format

Use sequential IDs starting from `TC001`:
- TC001, TC002, TC003, ...

## Required Fields

Each test case must include:

| Field | Description |
|-------|-------------|
| 序号 | TC001 format, incrementing |
| 模块 | Business module name |
| 前置条件 | Preconditions (array) |
| 执行步骤 | Execution steps (array) |
| 预期结果 | Expected results (array) |

## JSON Schema

```json
{
  "modules": [
    {
      "name": "模块名称",
      "cases": [
        {
          "id": "TC001",
          "title": "用例标题",
          "priority": "P0",
          "preconditions": ["前置条件1", "前置条件2"],
          "steps": ["步骤1", "步骤2"],
          "expected_results": ["预期结果1", "预期结果2"]
        }
      ]
    }
  ]
}
```

## Priority Mapping

- **P0**: Core business success path
- **P1**: Core negative and state constraints
- **P2**: Boundary and compatibility checks
- **P3**: Nice-to-have robustness checks

## Script Usage

```bash
python3 /Users/ivi/Dev/xmind/autocase/scripts/build_xmind_from_cases.py \
  --template /Users/ivi/Dev/xmind/模板-登录注册.xmind \
  --input /path/to/cases.json \
  --output /path/to/output.xmind \
  --root-title "功能测试用例"
```

## Quality Requirements

- Keep module boundaries clear
- Ensure each step is executable
- Ensure each expected result is observable
- Keep steps and expected results logically aligned
- Avoid vague language like "normal", "correct", "works" without measurable detail

## Output Format

XMind structure:
```
功能测试用例
├── 模块A
│   ├── TC001 用例标题1
│   │   ├── 模块: 模块A
│   │   ├── 优先级: P0
│   │   ├── 前置条件
│   │   │   ├── 1. 前置条件1
│   │   │   └── 2. 前置条件2
│   │   ├── 执行步骤
│   │   │   ├── 1. 步骤1
│   │   │   └── 2. 步骤2
│   │   └── 预期结果
│   │       ├── 1. 预期结果1
│   │       └── 2. 预期结果2
│   └── TC002 用例标题2
│       └── ...
└── 模块B
    └── ...
```

## References

- Schema: `/Users/ivi/Dev/xmind/autocase/references/case-schema.md`
- Rules: `/Users/ivi/Dev/xmind/autocase/references/generation-rules.md`
