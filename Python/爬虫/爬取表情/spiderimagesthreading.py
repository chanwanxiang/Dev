# coding: utf-8
__author__ = 'Mac'
__date__ = '2020/4/11 20:47'

'''
如果大家想要完成一个爬虫脚本的话
需要使用一个第三方库
    requests
    bs4
'''

# 创建文件夹的包 存储表情包文件的
import os
# 爬虫库
import requests
# 网页选择器
from bs4 import BeautifulSoup
# 队列
from queue import Queue
# 多线程包 
from threading import Thread


# 创建一个多线程类
class DownLoad_Images(Thread):
    # 重写构造函数
    def __init__(self, queue, path):
        Thread.__init__(self)
        self.queue = queue
        self.path = path

        if not os.path.exists(path):
            os.mkdir(path)

    #  重写run()方法
    def run(self):
        while True:
            url = self.queue.get()
            try:
                download_images(url, self.path)
            except:
                print('下载失败...')
            finally:
                # 线程在队列中取完元素之后或者程序退出之后发送一个结束信号
                self.queue.task_done()


# 爬虫代码
def download_images(url, path):
    # 定义请求头
    headers = {
        'User-Agent':
            'Mozilla/5.0(Macintosh;Intel MacOS X 10_15_4) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 80.0.3987.163Safari / 537.36'
    }
    response = requests.get(url, headers=headers)

    # 使用网页选择器去寻找图片资源
    '''
    soup网页选择器对象需要两个参数
        网页对象
        lxml：html解析库 让python可以控制html代码
    '''
    soup = BeautifulSoup(response.text, 'lxml')
    img_list = soup.find_all('img', class_='ui image lazy')
    # print(img_list)

    # 二次筛选
    for img in img_list:
        image_name = img.get('title')
        image_url = img.get('data-original')
        print(image_name, image_url)

        # 保存图片
        try:
            with open(path + image_name + os.path.splitext(image_url)[-1], 'wb') as f:
                img = requests.get(image_url, headers=headers).content
                f.write(img)
                print('下载成功: %s' % image_name)
        except:
            print('下载失败...')


if __name__ == "__main__":
    _url = 'https://fabiaoqing.com/biaoqing/lists/page/{page}.html'
    urls = [_url.format(page=page) for page in range(1, 201)]
    queue = Queue()
    path = './threadingimages/'

    # 创建线程
    for x in range(10):
        worker = DownLoad_Images(queue, path)

        # 创建守护线程
        '''
        如果子线程为守护线程的话 主线程结束时不会检测子线程是否结束任务
        直接退出
        '''
        worker.daemon = True
        worker.start()

    # 将网站链接压入队列
    for url in urls:
        queue.put(url)

    # 等队列为空 则退出所有线程
    queue.join()
    print('下载完毕....')