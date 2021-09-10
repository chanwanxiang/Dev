import os
import requests
# 网页选择器
from bs4 import BeautifulSoup
# 队列
from queue import Queue
# 多线程包
from threading import Thread


def imgdow(url, path):
    # 创建请求头
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }

    # 对网站进行请求
    response = requests.get(url, headers=headers)
    # print(response.text,type(response.text))  #<class 'str'>

    # 解析响应
    soup = BeautifulSoup(response.text, 'lxml')
    # print(soup,type(soup))  #<class 'bs4.BeautifulSoup'>
    imglist = soup.find_all('img', attrs={'class': 'ui image lazy'})
    # print(imglist,type(imglist))  #[.,.,.] <class 'bs4.element.ResultSet'>

    # 遍历数据,提取价值数据
    for img in imglist:
        imgName = img.get('title')
        imgUrl = img.get('data-original')
        print(imgName, imgUrl)

        # 保存数据
        try:
            # os.path.splitext 分离文件名和扩展名
            # response.text 返回的是一个unicode型的文本数据
            # response.content 返回的是bytes型的二进制数据

            with open(path + imgName + os.path.splitext(imgUrl)[-1], 'wb') as f:
                img = requests.get(imgUrl, headers=headers).content
                f.write(img)
                print(f'下载成功,{imgName}')
        except Exception as msg:
            print(f'下载失败,{msg}')

# 创建多线程类
class DownloadImg(Thread):
    # 重新__init__方法
    def __init__(self, queue, path):
        Thread.__init__(self)
        self.queue = queue
        self.path = path

        if not os.path.exists(path):
            os.mkdir(path)

    # 重写run方法
    def run(self):
        while True:
            # queue.get([block[,timeout]]) 获取队列,timeout等待时间
            url = self.queue.get()
            try:
                imgdow(url, self.path)
            except Exception as msg:
                print(f'下载失败,{msg}')
            finally:
                # 线程在队列中取完元素之后后者退出之后发送一个结束限号
                self.queue.task_done()


if __name__ == '__main__':
    urlName = 'https://fabiaoqing.com/biaoqing/lists/page/{pageNum}.html'
    urls = [urlName.format(pageNum=pageNum) for pageNum in range(1, 2)]
    # print(urls)

    queue = Queue()
    path = 'D:/wxchans/imgdow/'

    # 创建线程
    for x in range(3):
        rookie = DownloadImg(queue, path)

        # 创建守护线程
        # 如果子线程为守护线程的话,主线程结束时不会监测子线程是否结束任务直接退出
        rookie.daemon = True
        rookie.start()

    # 将url压入队列
    for url in urls:
        queue.put(url)

    # 等队列为空,则退出所有线程
    queue.join()
    print('下载完毕')
