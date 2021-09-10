# 创建是个线程,卖100张火车票

import time
import threading

# 获取线程锁
lock = threading.Lock()

numTik = 100

def sellTik():
    global numTik
    while numTik != 0:
        lock.acquire()
        if numTik > 0:
            time.sleep(0.1)
            numTik -= 1
            lock.release()
            print(f'{threading.current_thread().name}卖出了一张票,还剩{numTik}张')
        else:
            print('票已售罄')
            break


if __name__ == '__main__':
    for x in range(1, 10):
        newthread = threading.Thread(target=sellTik, name=f'窗口{x}')
        newthread.start()
