from selenium import webdriver

webChrome = webdriver.Chrome()

webChrome.get('https://signtest.yuuwei.com/')

name = webChrome.find_element_by_xpath(
    '//*[@id="app"]/div/div[2]/div[2]/div/form/div[1]/div/div/input').send_keys('admindlm')
pswd = webChrome.find_element_by_xpath(
    '//*[@id="app"]/div/div[2]/div[2]/div/form/div[2]/div/div/input').send_keys('yuwei@123456')

webChrome.find_element_by_xpath(
    '//*[@id="app"]/div/div[2]/div[2]/div/form/div[3]/div/button/span').click()

webChrome.implicitly_wait(10)

webChrome.maximize_window()
