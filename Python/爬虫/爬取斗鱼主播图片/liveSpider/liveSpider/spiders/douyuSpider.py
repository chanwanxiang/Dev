import json
import scrapy
from liveSpider.items import LivespiderItem

class DouyuspiderSpider(scrapy.Spider):
    name = 'douyuSpider'
    allowed_domains = ['www.douyu.com']
    base_url = 'https://m.douyu.com/api/room/list?page={}&type=yz'
    offset = 0
    start_urls = [base_url.format(offset)]

    def parse(self, response):
        # 提取数据
        data_list = json.loads(response.body)['data']
        print(data_list)
        if data_list:
            for data in data_list:
                item = LivespiderItem()
                item['nickname'] = data['nickname'].encode('utf-8')
                item['vertical_src'] = date['verticalSrc']

                yield item

            self.offset += 1
            url = self.base_url.format(self.offset)

            # 回调自身
            yield scrapy.Request(url,callback=self.parse,dont_filter=True)
            