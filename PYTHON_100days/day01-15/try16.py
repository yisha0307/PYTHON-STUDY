# from time import time

# def main():
#     sum = 0
#     # 创建这个list耗费了不少时间
#     number_list = [x for x in range(1, 100000001)]
#     start = time()
#     for i in number_list:
#         sum += i
#     end = time()
#     print('总和为%d, 共耗时%.4f秒' % (sum, end-start))

# if __name__ == '__main__':
#     main()

from multiprocessing import Process, Queue
from random import randint
from time import time

def task_handler(curr_list, result_queue):
    total = 0
    for number in curr_list:
        total += number
    result_queue.put(total)

def main():
    processes = []
    number_list = [x for x in range(1, 100000001)]
    # Queue: 被多个进程共享的队列
    result_queue = Queue()
    index = 0
    # 启动8个进程将数据切片后进行运算
    for _ in range(8):
        p = Process(target=task_handler, args=(number_list[index:index+12500000], result_queue))
        index += 12500000
        processes.append(p)
        p.start()
    start = time()
    for t in processes:
        t.join()
    # 合并执行结果
    total = 0
    while not result_queue.empty():
        total += result_queue.get()
    end = time()
    print('total={0}, time={1}'.format(total, end-start))

if __name__ == '__main__':
    main()