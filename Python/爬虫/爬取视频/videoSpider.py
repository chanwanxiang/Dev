# 爬虫步骤
#     1. 获取数据源
#     2. 向数据源发送数据请求
#     3. 解析数据
#     4. 保存数据


# 前端技术:
#     ajax异步加载请求
#     在不需要刷新整个野蛮的情况下,对页面进行局部刷新

import requests
import re
import os
import pprint


def videoSpider(url):
    # 请求头中用户凭证
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }

    # 获取数据
    response = requests.get(url, headers)
    jsonData = response.json()
    pprint.pprint(jsonData)

    # 创建文件夹
    os.makedirs('video/')

    # 解析数据(视频地址)
    datalist = jsonData['content']['list']

    for data in datalist:
        videoTitle = data['alias']
        videoUrl = data['playurl']
        # 去除标题中的非法字符
        pattern = re.compile("[^\u4e00-\u9fa5^.^a-z^A-Z^0-9]")
        newTitle = re.sub(pattern, '', videoTitle)

        # 请求视频数据
        videoData = requests.get(url=videoUrl, headers=headers).content

        # 数据保存
        with open('video/' + newTitle + os.path.splitext(videoUrl)[-1], 'wb+') as f:
            f.write(videoData)
            print('保存完成' + newTitle)


if __name__ == '__main__':
    # 获取的数据源
    urlOri = 'http://www.6.cn/minivideo/getMiniVideoList.php?act=recommend&page={page}&pagesize=20'
    urls = [urlOri.format(page=page) for page in range(1, 2)]
    for url in urls:
        videoSpider(url)
