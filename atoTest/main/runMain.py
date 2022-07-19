from selenium import webdriver

path = 'D:\Dev\chromedriver.exe'

# 不开网页
# browser = webdriver.ChromeOptions()

# 打开网页
browser = webdriver.Chrome(path)

browser.get('https://www.baidu.com')

