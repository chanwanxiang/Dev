from playwright.sync_api import sync_playwright

input('1....')
# 启动 playwright driver 进程
p = sync_playwright().start()

input('2....')
# 启动浏览器，返回 Browser 类型对象
browser = p.chromium.launch(headless=False)

# 创建新页面，返回 Page 类型对象
page = browser.new_page()
page.goto("https://www.byhy.net/_files/stock1.html")
print(page.title()) # 打印网页标题栏

# 输入通讯，点击查询

# 通过id定位，#
page.locator('#kw').fill('通讯')  # 输入通讯
page.locator('#go').click()      # 点击查询

# 通过class定位，同时拥有两个class属性
page.locator('.student').all()
page.locator('.male.student')

# 通过tag定位
page.locator('div').all()

# 通用元素定位方法，根据属性选择 []
page.locator('[href="https//:baidu.com"]')
# 可在前面加上标签名称限制
page.locator('a[href="https://baidu.com"]')
# 支持正则
page.locator('[href*="baidu"]') # 包含baidu
page.locator('[href^="http"]') # http开头
page.locator('[href$=".com"]') # .com结尾

#  选择子元素和后代元素
page.locator('.student > .male').all() # 直接子元素为male类
page.locator('.student .male').all() # 后代元素为male类

# xpath定位
# 路径定位 绝对路径、相对路径
# 利用元素属性定位
# 层级与属性结合定位
# 属性与逻辑定位结合

# 语法 //标签名[@属性=‘value’]
# ‘/’代表从子节点寻找，‘//’代表从当前标签下的所有后代节点寻找 //sapn[caontains(@class, 'name')]
# 属性以什么开头 //标签名[start-with(@属性, 'value')]
# 文本值=什么属性 //标签名[text()='value']

# 打印所有搜索内容
lcs = page.locator(".result-item").all()
for lc in lcs:
    print(lc.inner_text())

input('3....')
# 关闭浏览器
browser.close()
input('4....')
# 关闭 playwright driver 进程
p.stop()

//label[text()='贷款银行']/following::div[position()=2]