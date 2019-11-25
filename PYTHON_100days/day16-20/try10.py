'''
多进程:
多进程和进程池
多线程因为GIL的存在不能够发挥CPU的多核特性
对于计算密集型任务应该考虑使用多进程
'''
import concurrent.futures
from time import time
import math

PRIMES = [
    1116281,
    1297337,
    104395303,
    472882027,
    533000389,
    817504243,
    982451653,
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419
] * 5

def is_prime(n):
    # 判断素数
    if n % 2 == 0:
        return False
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False
    return True

def main():
    start = time()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print(f'{number} is prime: {prime}')
    print(f'共耗费时间{time() - start}秒')

if __name__ == '__main__':
    main()