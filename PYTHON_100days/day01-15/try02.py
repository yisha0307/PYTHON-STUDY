sum = 0
for x in range(1, 101):
    if x % 2 == 0:
        sum += x
print(sum)

# import random
# answer = random.randint(1, 100)
# counter = 0
# while True:
#     counter += 1
#     number = int(input('请输入: '))
#     if number < answer:
#         print('大一点')
#     elif number > answer:
#         print('小一点')
#     else:
#         print('恭喜你猜对了')
#         break
# print('您总共猜了%d次' % counter)

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('%d * %d = %d' % (i, j, i*j), end ='\t')
#     print()

# print('1-------------------')
# from math import sqrt
# num = int(input('请输入一个正整数：'))
# end = int(sqrt(num))
# is_prime = True
# for x in range(2, end + 1):
#     if num % x == 0:
#         is_prime = False
#         break
# if is_prime and num != 1:
#     print('%d是素数' % num)
# else:
#     print('%d不是素数' % num)

# print('2-----------------')
# x = int(input('x= '))
# y = int(input('y= '))
# if x > y:
#     # 如果x>y就交换位置
#     x, y = y, x
# for factor in range(x, 0, -1):
#     if x % factor == 0 and y % factor == 0:
#         print('%d和%d的最大公约数是%d' % (x, y, factor))
#         print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
#         break

print('3-----------------')
row = int(input('请输入行数: '))
for i in range(row):
    for _ in range(i+1):
        print('*', end='')
    print()

for i in range(row):
    for j in range(row):
        if j < row - i -1:
            print(' ', end ='')
        else:
            print('*', end ='')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end = '')
    for _ in range(2 * i + 1):
        print('*', end ='')
    print()
