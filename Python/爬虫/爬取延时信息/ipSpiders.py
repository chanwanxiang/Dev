#!/usr/bin/env python
# encoding=utf-8

import requests
import re
import time

start = time.time()

def get_ips():
    #url = "https://www.ping.cn/ping/sellercentral.amazon.com"
    #url = "https://www.ping.cn/ping/sellercentral.amazon.jp"
    #url = "https://www.ping.cn/ping/sellercentral.amazon.de"
    url = "https://www.ping.cn/ping/sellercentral.amazon.co.uk"

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
    }
    response = requests.get(url=url, headers=header)
    ips = re.findall('<td>(.*?)</td>', response.text)
    print(ips)
    ips_set = {i for i in ips if len(i) > 7}
    return ips_set

if __name__ == '__main__':
    ips = get_ips()
    for ip in ips:
        print(ip)
    # print(time.time() - start)
