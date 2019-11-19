print('1/寻找水仙花数-------------------')
"""
说明：水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，
它是一个3位数，
该数字每个位上数字的立方之和正好等于它本身，例如：$1^3 + 5^3+ 3^3=153$
"""
results = []
for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if low**3 + mid**3 + high**3 == num:
        results.append(num)
print(results)

print('2/正整数反转-------------------')
num = int(input('请输入数字num = '))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)

print('3/百钱百鸡问题-------------------')
for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if 5 * x + 3 * y + z/3 == 100:
            print('公鸡{0}只， 母鸡{1}只，小鸡{2}只'.format(x,y,z))

print('4/CRAPS赌博游戏-------------------')
from random import randint
money = 1000
while money > 0:
    needs_go_on = False
    while True:
        debt = int(input('您目前的财产为%d, 请下注: ' % money))
        if 0 < debt <= money:
            break
    first = randint(1, 6) + randint(1, 6)
    print('玩家摇出了%d' % first)
    if first == 7 or first == 11:
        print('玩家胜!')
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('庄家胜!')
        money -= debt
    else:
        needs_go_on = True
    while needs_go_on:
        needs_go_on = False
        current = randint(1, 6) + randint(1, 6)
        print('玩家摇出了%d点' % current)
        if current == 7:
            print('庄家胜！')
            money -= debt
        elif current == first:
            print('玩家胜！')
            money += debt
        else:
            needs_go_on = True
print('你破产了，游戏结束！')

print('5/斐波那契数列的前20个数-------------------')
a = 1
b = 1
results = [a, b]
for i in range(20):
    a, b = b, a+b
    results.append(b)
print(results)

print('6/找出10000以内的完美数-------------------')
# for i in range(2, 10001):
#     result = 0
#     for j in range(1, i):
#         if i % j == 0:
#             result += j
#     if result == i:
#         print(i)

print('7/输出100以内所有的素数-------------------')
import math
for i in range(2, 101):
    is_prime = True
    j = int(math.sqrt(i))
    for nn in range(2, j + 1):
        if i % nn == 0:
            is_prime = False
            break
    if is_prime:
        print(i, end=' ')
print()
    