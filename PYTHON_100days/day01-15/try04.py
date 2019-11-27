# 输入M和N计算C(M,N)

# m = int(input('m = '))
# n = int(input('n = '))
# def factorial(num):
#     # 求阶乘
#     result = 1
#     for n in range(1, num + 1):
#         result *= n
#     return result
# print(factorial(m) // factorial(n) // factorial(m-n))

from random import randint
def roll_dice(n = 2):
    # 摇色子
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total

def add (a=0, b=0, c=0):
    # 三个数相加
    return a+b+c

print(roll_dice())
print(roll_dice(3))
print(add())
print(add(1, 2))
print(add(1, 2, 3))
print(add(a = 50, b = 100, c = 50))

def sum(*args):
    total = 0
    for i in args:
        total += i
    return total
print(sum(1,3,5,10,20))


print('PRACTICE 1: 实现计算求最大公约数和最小公倍数的函数-----')
def gcd(x, y):
    if x>y:
        # 如果x>y就交换位置
        x, y = y, x
    for i in range(x, 0, -1):
        if x % i == 0 and y % i == 0:
            return i
def lcm(x, y):
    return x * y // gcd(x, y)

print('PRACTICE2: 实现判断一个数是不是回文数的函数-------')
def is_palindrome(num):
    original = num
    reversed = 0
    while num > 0:
        reversed = reversed * 10 + num % 10
        num //= 10
    return original == reversed
print(is_palindrome(12321))

print('PRACTICE3: 实现判断一个数是不是素数的函数----------')
def is_prime(num):
    for factor in range(2, num):
        if num % factor == 0:
            return False
    if num != 1:
        return True
    else:
        return False

print(is_prime(2057))

print('PRACTICE4: 写一个程序判断输入的正整数是不是回文素数---------')
num = int(input('请输入正整数: '))
if is_prime(num) and is_palindrome(num):
    print('%d是回文素数' % num)
else:
    print('%d不是回文素数' % num)