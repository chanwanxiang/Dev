---
name: autocase
description: Generate detailed functional test cases by module from requirement text or prototype notes, then export an XMind file that can be opened in XMind software. Use when the user asks to produce module-based test cases with fixed fields (module, priority, preconditions, steps, expected results) and mind-map output.
---

# AutoCase

## Workflow

1. Parse requirement text or prototype notes and extract modules plus feature points.
2. Generate test cases with standard coverage depth:
   - 1 normal path
   - 1 key abnormal path
   - 1 key boundary path
3. Build structured JSON with this exact shape:
   - `modules[].name`
   - `modules[].cases[].title`
   - `modules[].cases[].priority` (`P0|P1|P2|P3`)
   - `modules[].cases[].preconditions[]`
   - `modules[].cases[].steps[]`
   - `modules[].cases[].expected_results[]`
4. Run `scripts/build_xmind_from_cases.py` with template input and output path.
5. Return the generated `.xmind` file path.

## Output Contract

Keep case grouping as `模块 -> 用例`.

For each case node, create these five direct child fields:

1. `模块: xxx`
2. `优先级: Pn`
3. `前置条件`
4. `执行步骤`
5. `预期结果`

Under `前置条件/执行步骤/预期结果`, create numbered child nodes.

## Quality Requirements

- Keep module boundaries clear.
- Ensure each step is executable.
- Ensure each expected result is observable.
- Keep steps and expected results logically aligned.

## Script Usage

```bash
python3 scripts/build_xmind_from_cases.py \
  --template assets/template-login-register.xmind \
  --input /path/to/cases.json \
  --output /path/to/output.xmind \
  --root-title "功能测试用例"
```

## References

- Schema and field constraints: `references/case-schema.md`
- Coverage and priority rules: `references/generation-rules.md`
