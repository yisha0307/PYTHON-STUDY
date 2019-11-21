from multiprocessing import Process, Queue
from time import time, sleep

def sub_task(name, result_queue):
    # Queue在macos不能用qsize()
    while not result_queue.full():
        print(name, end =' ')
        result_queue.put(name)
        sleep(0.01)

def main():
    result_queue = Queue(10)
    p1 = Process(target=sub_task, args=('ping', result_queue))
    p1.start()
    p2 = Process(target=sub_task, args=('pong', result_queue))
    p2.start()
    for p in [p1, p2]:
        p.join()
    print('完成--------')

if __name__ == '__main__':
    main()