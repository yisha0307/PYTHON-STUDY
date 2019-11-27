'''
100个线程向同一个银行账户转账（转入1元钱）的场景
银行账户就是一个临界资源
@临界资源: 一个资源被多个线程竞争使用
'''
from time import sleep
from threading import Thread, Lock

class Account(object):
    # 只有获得锁的线程才能访问临街资源
    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        # 先获取锁才能执行后续的代码
        # 保护临界资源
        self._lock.acquire()
        try:
            new_balance = self._balance+money
            sleep(0.01)
            self._balance = new_balance
        finally:
            # 在finally里执行释放锁的操作
            self._lock.release()

    @property
    def balance(self):
        return self._balance

class AddMoneyThread(Thread):
    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money
    def run(self):
        self._account.deposit(self._money)

def main():
    account = Account()
    threads = []
    # 创建100个线程存钱
    for _ in range(100):
        t = AddMoneyThread(account ,1)
        threads.append(t)
        t.start()
    # 等所有存钱线程执行完毕:
    for t in threads:
        t.join()
    print('账户余额为%d' % account.balance)

if __name__ == '__main__':
    main()
