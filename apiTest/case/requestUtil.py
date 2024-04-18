import json
import pprint
import requests


# from util import

# HTTP工具类封装 每个请求需要做异常捕获,日志记录,协议转换,封装工具方便进行统一维护


class RequestUtil:
    def sendrequest(self, url, method, headers=None, params=None, contentType=None):
        try:
            if method.upper() == 'GET':
                result = requests.get(
                    url=url, params=params, headers=headers).json()
                return result
            elif method.upper() == 'POST':
                if contentType.upper() == 'DATA':
                    result = requests.post(
                        url=url, data=params, headers=headers, verify=False).json()
                else:
                    result = requests.post(
                        url=url, json=params, headers=headers, verify=False).json()
                return result
            else:
                print('不支持的请求方式')

        except Exception as e:
            print('HTTP请求报错:{0}'.format(e))


if __name__ == "__main__":
    # url = 'https://api.xdclass.net/pub/api/v1/web/all_category'
    # r = RequestUtil()
    # result = r.request(url,'get')
    # pprint.pprint(result)

    # url = 'https://api.xdclass.net/pub/api/v1/web/web_login'
    url = 'https://signtest.yuuwei.com/bank/fv/detail/2024020111140001'
    r = RequestUtil()
    headers = {'Content-Type': 'application/x-www-form-urlencoded',
               'token': 'c168930f-fde4-4e6c-b961-243195469802'}
    # data = {'phone': '13113777555', 'pwd': '1234567890'}
    result = r.request(url, 'get', headers=headers)
    pprint.pprint(result)
