# Python中的多进程
# 使用同一进程
# from random import randint
# from time import time, sleep

# def download_task (filename):
#     print('开始下载{0}...'.format(filename))
#     s = randint(5, 10)
#     sleep(s)
#     print('{0}下载完成！共耗时{1}秒'.format(filename, s))

# def main():
#     start = time()
#     download_task("Python从入门到住院.pdf")
#     download_task("peking hot.avi")
#     end = time()
#     print('总共耗时%d秒' % (end-start))

# if __name__ == '__main__':
#     main()

# 使用多进程
from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep

def download_task(filename):
    print('开始下载{0}, 进程号{1}'.format(filename, getpid()))
    time_to_download = randint(5, 8)
    sleep(time_to_download)
    print('%s下载完成！耗费%d秒！' % (filename, time_to_download))

def main():
    start = time()
    '''
    Process创建进程对象
    target传入一个函数表示进程启动后要执行的代码
    args是元组，传递给参数的参数
    start(): 开始进程
    join(): 等待进程执行结束
    '''
    p1 = Process(target=download_task, args = ('Python从入门到住院.pdf', ))
    p1.start()
    p2 = Process(target=download_task, args = ('peking hot.avi', ))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('总共耗时%d秒' % (end-start))

if __name__ == '__main__':
     main()