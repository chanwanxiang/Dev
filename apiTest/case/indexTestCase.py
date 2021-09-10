import os
import sys
import unittest
from util.requestUtil import RequestUtil

sys.path.append('../apiTest')

# 主机地址
host = 'https://api.xdclass.net'


# 首页测试用例案例
class indexTestCase(unittest.TestCase):

    # 首页分类列表
    def testindexCategorylist(self):
        # 创建request对象
        req = RequestUtil()

        # 首页模块 分类列表
        url = host + '/pub/api/v1/web/all_category'
        response = req.request(url, 'get')

        # 判断响应的状态码是否正常 断言
        self.assertEqual(response['code'], 0, '业务状态码不正常')

        # 判断分类列表长度 断言
        self.assertTrue(len(response['data']) > 0, '首页分类列表为空')
        pass

    # 首页视频列表
    def testindexVideolist(self):
        req = RequestUtil()

        # 首页模块 分类列表
        url = host + '/pub/api/v1/web/index_card'
        response = req.request(url, 'get')

        # 判断响应的状态码是否正常
        self.assertEqual(response['code'], 0, '业务状态码不正常')

        # 判断视频卡片列表长度
        self.assertTrue(len(response['data']) > 0, '视频卡片列表为空')
        videoCardlist = response['data']

        # 判断视频卡片列表长度并返回错误值
        for card in videoCardlist:
            self.assertTrue(len(card['title']) > 0,
                            '视频卡片标题为空,id=' + str(card['id']))


if __name__ == "__main__":
    unittest.main(verbosity=2)
