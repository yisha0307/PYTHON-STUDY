import time
from threading import Thread, Lock

from concurrent.futures import ThreadPoolExecutor

class Account(object):
    def __init__(self):
        self.balance = 0
        self.lock = Lock()
    def deposit(self, money):
        # 保护临界资源
        with self.lock:
            new_balance = self.balance + money
            time.sleep(0.001)
            self.balance = new_balance

class AddMoneyThread(Thread):
    def __init__(self, account, money):
        self.account = account
        self.money = money
        super().__init__()
    def run(self):
        # 线程开始之后run的函数
        self.account.deposit(self.money)

def main():
    account = Account()
    threads = []
    pool = ThreadPoolExecutor(max_workers=10)
    for _ in range(100):
        # 第一种
        # t = AddMoneyThread(account, 1)
        # threads.append(t)
        # t.start()
        # 第二种
        # t = Thread(target=account.deposit, args=(1,))
        # threads.append(t)
        # t.start()
        # 第三种 利用线程池
        t = pool.submit(account.deposit, 1)
        threads.append(t)
    pool.shutdown()
    # for t in threads:
    #     t.join()
    for t in threads:
        t.result()
    print(account.balance)

if __name__ == '__main__':
    main()