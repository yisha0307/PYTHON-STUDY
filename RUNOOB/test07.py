# 循环
# fibonacci series
a, b = 0, 1
while b<1000:
    print(b, end=',')
    a,b = b, a+b
print('')
print('---------------------')

# age = int(input("请输入你家狗狗的年龄: "))
# print("")
# if age <= 0:
#         print("你是在逗我吧!")
# elif age == 1:
#         print("相当于 14 岁的人。")
# elif age == 2:
#         print("相当于 22 岁的人。")
# else:
#     human = 22 + (age - 2) * 5
#     print("对应人类年龄： ", human)

# # 退出提示
# input("点击enter退出")

# number = 7
# guess = -1
# str = '数字猜谜游戏'
# print(str.center(40, '*'))
# while number != guess:
#     guess = int(input("请输入你猜的数字："))

#     if guess == number:
#         print("恭喜，你猜对了！")
#     elif guess < number:
#         print("猜的数字小了...")
#     elif guess > number:
#         print("猜的数字大了...")

n = 100
sum = 0
counter = 1
while counter <= n:
    sum += counter
    counter += 1

print("1到%d只和为：%d" % (n, sum))

count = 5
while count <= 5:
    print(count, '小于或等于5')
    count += 1
else:
    print(count, "大于5")

languages = ['C', 'C++', 'Perl', 'Taobao']
for lan in languages:
    if lan == 'Perl':
        print('Perl!')
        break
    print('循环数据 ' + lan)
else:
    print("没有循环数据！")
print("完成循环！")

for i in range(0, 10, 3):
    print(i)

for i in range(-10, -100, -30):
    print(i)

for i in range(len(languages)):
    print(i, languages[i])

print(list(range(5)))

for n in range(2, 10):
    # 如果不能被前面的每一个数字整除，就认为是质数
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        print(n, ' 是质数')

for letter in 'Runoob':
    if letter == 'o':
        pass
        print('执行pass')
    print('当前字母 ：', letter)
print('Good bye!')