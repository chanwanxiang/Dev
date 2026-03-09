# AutoCase JSON Schema (Practical)

Use this structure as the fixed intermediate input for `scripts/build_xmind_from_cases.py`.

## Root object

- `modules` (array, required, non-empty)

## Module object

- `name` (string, required, non-empty)
- `cases` (array, required, non-empty)

## Case object

- `title` (string, required, non-empty)
- `priority` (string, required): one of `P0`, `P1`, `P2`, `P3`
- `preconditions` (array of string, required, non-empty)
- `steps` (array of string, required, non-empty)
- `expected_results` (array of string, required, non-empty)

## Example

```json
{
  "modules": [
    {
      "name": "登录/注册",
      "cases": [
        {
          "title": "已注册手机号+正确验证码登录成功",
          "priority": "P0",
          "preconditions": [
            "账号已注册",
            "验证码服务可用"
          ],
          "steps": [
            "进入登录页",
            "输入已注册手机号",
            "获取验证码并输入正确验证码",
            "勾选协议，点击登录"
          ],
          "expected_results": [
            "登录成功",
            "跳转到登录前触发页面"
          ]
        }
      ]
    }
  ]
}
```

## Validation behavior

- Script rejects missing/empty fields.
- Script returns path-aware errors, for example:
  - `Invalid input at modules[0].cases[1].priority: expected one of P0, P1, P2, P3`
