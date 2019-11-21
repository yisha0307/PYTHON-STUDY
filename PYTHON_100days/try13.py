# Python中的多线程
from random import randint
from threading import Thread
from time import time, sleep

# def download(filename):
#     print('开始下载%s...' % filename)
#     time_to_download = randint(5, 8)
#     sleep(time_to_download)
#     print('%s下载完成！共耗费%d秒！' % (filename, time_to_download))

# def main():
#     start = time()
#     '''
#     Thread传参和Process一样
#     '''
#     t1 = Thread(target = download, args=('Python从入门到住院.pdf',))
#     t1.start()
#     t2 = Thread(target=download, args=('peking hot.avi',))
#     t2.start()
#     t1.join()
#     t2.join()
#     end = time()
#     print('总共耗时%d秒' % (end-start))

# if __name__ == '__main__':
#     main()

# 创建自定义线程
class DownloadThread (Thread):
    def __init__(self, filename):
        super().__init__()
        self._filename = filename
    def run(self):
        print('开始下载%s...' % self._filename)
        time_to_download = randint(5, 8)
        sleep(time_to_download)
        print('%s下载完成！共耗费%d秒！' % (self._filename, time_to_download))

def main():
    start = time()
    t1 = DownloadThread('Python从入门到住院.pdf')
    t1.start()
    t2 = DownloadThread('peking.avi')
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗时%d秒' % (end-start))

if __name__ == '__main__':
     main()
