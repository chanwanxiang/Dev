import os
import parsel
import requests


class BaiduSpider():

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'}

    def __init__(self, path):
        # 初始化url和路径
        self.path = path

    def spiderAction(self):
        # 贴吧入口
        urlOri = 'https://tieba.baidu.com/f?kw=%E7%BA%A6%E4%BC%9A&ie=utf-8&pn={page}'
        # 分页爬取
        urls = [urlOri.format(page=page*50) for page in range(10)]
        print(urls)

        for url in urls:
            response = requests.get(url=url, headers=self.headers).text

        # 转换数据类型
        selector = parsel.Selector(response)

        # 全部帖子地址
        hreflist = selector.xpath(
            '//ul[@class="threadlist_bright j_threadlist_bright"]/li//div[@class="t_con cleafix"]//div[@class="threadlist_lz clearfix"]/div/a/@href').getall()

        # 拼接帖子地址
        for href in hreflist:
            allUrl = 'https://tieba.baidu.com' + href
            print('当前帖子链接:', allUrl)

            responseSecond = requests.get(
                url=allUrl, headers=self.headers).text
            selectorSecond = parsel.Selector(responseSecond)

            imgslist = selectorSecond.xpath(
                '//cc/div//img[@class="BDE_Image"]/@src').getall()
            print(imgslist)

            for imgs in imgslist:
                imgdata = requests.get(url=imgs, headers=self.headers).content

                fileName = imgs[-10:]

                with open(self.path + fileName, 'wb') as f:
                    f.write(imgdata)
                    print('爬取成功', fileName)


if __name__ == '__main__':

    savePath = 'imgs/'
    spider = BaiduSpider(savePath)
    spider.spiderAction()
