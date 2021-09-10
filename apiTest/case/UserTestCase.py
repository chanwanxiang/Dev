import sys
import requests
import unittest
from util.requestUtil import RequestUtil

sys.path.append('../apiTest')

# 用户测试用例
class UserTestCase(unittest.TestCase):

    # 用户测试登录用例
    def testUserlogin(self):
        url = 'https://api.xdclass.net/pub/api/v1/web/web_login'
        req = RequestUtil()
        data = {'phone': '13113777555', 'pwd': '1234567890'}
        response = req.request(url, 'post', params=data)
        self.assertEqual(response['code'], 0, '登录的状态码错误')


if __name__ == "__main__":
    unittest.main(verbosity=2)
