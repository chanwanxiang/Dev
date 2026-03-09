# AutoCase Generation Rules

Apply these rules when converting requirement text or prototype notes into functional test cases.

## Module splitting

- Split test cases by business module first, then by feature point.
- Keep each case inside one module only.
- Merge duplicate feature points before generating cases.

## Standard coverage depth

For each feature point, generate at least:

- 1 normal path case
- 1 key abnormal case (invalid input or wrong state)
- 1 key boundary case (empty/length/count/time-window)

## Priority mapping

- Main business success path: `P0` or `P1`
- Core negative and state constraints: `P1`
- Boundary and compatibility checks: `P2`
- Nice-to-have robustness checks: `P3`

Prefer higher priority when uncertain.

## Case writing quality

- Preconditions must be runnable and verifiable.
- Steps must be explicit and ordered.
- Expected results must map to key steps and be observable.
- Avoid vague language like "normal", "correct", "works" without measurable detail.

## Prototype-driven extraction

- Read screens, components, and interaction flows from prototype notes.
- Convert UI controls (input/button/dialog/countdown/link) into testable feature points.
- If prototype text is missing, infer from interaction semantics and annotate assumptions in the generated case text.

## XMind node format (fixed)

Inside each case node, always create exactly five direct child fields:

1. `模块: <模块名>`
2. `优先级: <Pn>`
3. `前置条件`
4. `执行步骤`
5. `预期结果`

For `前置条件/执行步骤/预期结果`, add numbered child nodes (`1. ...`, `2. ...`).
