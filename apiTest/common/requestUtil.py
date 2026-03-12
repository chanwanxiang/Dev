import yaml
import pprint
import requests
from requests import utils
from util.tools import FILE_PATH
from common.logUtil import logs


class RequestUtil:
    def __init__(self):
        self.logger = logs

    def sendRequest(self, **kwargs):
        cookies = {}
        session = requests.Session()
        resp = session.request(**kwargs)
        setcookies = requests.utils.dict_from_cookiejar(resp.cookies)
        if setcookies:
            cookies['cookies'] = setcookies
            open(FILE_PATH['extract'], 'a', encoding='utf-8').write(yaml.dump(cookies))
            logs.info(f'写入extract文件数据:{yaml.dump(cookies)}')
            logs.info(f'接口实际返回信息{resp.json()}')

        return resp.json(), resp.status_code

    def runMain(self, apiname, casename, url, method, headers, cookies, files, **kwargs):
        logs.info(f'接口名称{apiname}')
        logs.info(f'接口地址{url}')
        logs.info(f'请求方式{method}')
        logs.info(f'请求头部信息{headers}')
        logs.info(f'请求参数{kwargs}')
        resp = self.sendRequest(url=url, method=method, headers=headers, cookies=cookies, files=files, verify=False,
                                **kwargs)

        return resp


if __name__ == "__main__":
    url = 'http://127.0.0.1:8787/dar/user/login'
    # url = 'http://127.0.0.1:8787/coupApply/cms/goodsList'
    r = RequestUtil()
    params = {'user_name': 'test01', 'passwd': 'admin123'}
    # params = {'msgType': 'getHandsetListOfCust'}
    result = r.request(url=url, method='post', params=params)
    pprint.pprint(result)
