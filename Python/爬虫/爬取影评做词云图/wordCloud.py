import os
import sys
import jieba
import parsel
import imageio
import requests
import os.path as op
from wordcloud import WordCloud


class MovieWordCloud():

    def getData(self):

        urlN = 'https://movie.douban.com/subject/34841067/comments?start={page}&limit=20&status=P&sort=new_score'
        urls = [urlN.format(page=x*20) for x in range(10)]

        headers = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
        }

        for url in urls:
            response = requests.get(url=url, headers=headers).text

        selector = parsel.Selector(response)
        commentlist = selector.xpath('//span[@class="short"]/text()').getall()

        try:
            with open(op.join(sys.path[0], '你好,李焕英.txt'), 'a', encoding='utf-8') as f:
                for comment in commentlist:
                    f.write(comment.replace('\n', ''))
                    f.write('\n')
                print('影评爬取完成')
        except Exception as msg:
            print(f'影评爬取失败{msg}')

    def makeWord(self):
        with open(op.join(sys.path[0], '你好,李焕英.txt'), 'r', encoding='utf-8') as f:
            details = f.read()
        detailslist = jieba.lcut(details)
        detailstring = ' '.join(detailslist)

        # op.join 把目录和文件名合成一个路径
        img = imageio.imread(op.join(sys.path[0], '贾玲.png'))  # 词云图的轮廓

        # 词云图的设置
        wc = WordCloud(
            width=1000,  # 图片宽度
            height=800,  # 图片高度
            font_path='msyh.ttc',  # 微软雅黑 系统自带
            mask=img,  # 词云图所用的图片
            scale=15,
            stopwords=set([line.strip() for line in open(
                op.join(sys.path[0], 'cnStopwords.txt'), 'r', encoding='utf-8')])
        )

        wc.generate(detailstring)
        wc.to_file(op.join(sys.path[0], 'wordcloud.png'))


if __name__ == '__main__':
    mwc = MovieWordCloud()
    # mwc.getData()  #爬虫,需要时候才爬
    # mwc.makeWord()

# 引申:os.path和sys.path的区别
# os.path    主要适用于对系统路径文件的操作
# sys.path   主要是对Python解释器的系统环境参数的操作(动态的改变Python解释器搜索路径)

# print(sys.path)  #['d:\\wxchans\\isMe\\Read-Search-Ask\\【1】Python\\爬虫\\你好,李焕英影评爬取词云图制作', 'D:\\python\\python37.zip', 'D:\\python\\DLLs', 'D:\\python\\lib', 'D:\\python', 'C:\\Users\\Admin\\AppData\\Roaming\\Python\\Python37\\site-packages', 'D:\\python\\lib\\site-packages', 'D:\\python\\lib\\site-packages\\pip-21.0-py3.7.egg']
