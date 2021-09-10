# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from itemadapter import ItemAdapter

class LivespiderPipeline(ImagesPipeline):

    def get_media_requests(self,item,info):
        image_link = item['vertical_src']
        yield scrapy.Request(image_link)

    def item_completed(self,result,item,info):
        path = r'D:\Coding-Always\Read-Search-Ask\Python\爬虫\爬取斗鱼主播图片\images\'

        if result[0][0] == True:
            os.rename(path + result[0][1]['path'],path + str(item('nickname')) + '.jpg')

        return item
