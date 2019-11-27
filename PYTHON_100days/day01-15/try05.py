list1 = [1, 3, 5, 7, 100]
for index, elem in enumerate(list1):
    print(index, elem)

f = [x for x in range(1, 10)]
print(f)

g = [x + y for x in 'ABCDE' for y in '1234567']
print(g)

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
        # yield 生成器
        yield a
# def main():
#     for val in fib(20):
#         print(val)
# if __name__ == '__main__':
#     main()

print(dict(zip(['a', 'b', 'c'], '123')))

item3 = {num: num ** 2 for num in range(1, 10)}
print(item3)

scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
for key in scores:
    print(f'{key}: {scores[key]}')
scores.update(冷面=67, 方启鹤=85)
print(scores, scores.get('冷面'))
scores.popitem()
print(scores)
print(scores.pop('骆昊', 100))

# print('PRACTICE1: 在屏幕上显示跑马灯文字------------')
# import os
# import time
# def main():
#     content = '北京欢迎你为你开天辟地…………'
#     while True:
#         os.system('cls')
#         print(content)
#         time.sleep(0.2)
#         content = content[1:]+content[0]
# if __name__ == '__main__':
#     main()

print('PRACTICE2: 设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成------------')
import random
def generate_code(code_len=4):
    code = ''
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbs = len(all_chars) - 1
    for _ in range(code_len):
        index = random.randint(0, numbs)
        code += all_chars[index]
    return code
print(generate_code(10))

print('PRACTICE3: 设计一个函数返回给定文件名的后缀名---------')
def get_suffix(filename, has_dot = False):
    # has_dot：返回的后缀名是否需要带点
    pos = filename.find('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''
print(get_suffix('filename.dot'))

print('PRACTICE4: 设计一个函数返回传入的列表中最大和第二大的元素的值---------')
def findMax(arr):
    sortedArr = sorted(arr, reverse=True)
    print('最大的是{0}, 第二大的是{1}'.format(sortedArr[0], sortedArr[1]))
findMax([99,87,90,12,1002])

print('PRACTICE5: 计算指定的年月日是这一年的第几天--------------')
def is_leap_year(year):
    # 判断是不是闰年
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def which_day(year, month, day):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    totaldays = 0
    if 2 < month <= 12:
        for j in range(month - 1):
            totaldays += months[j]
        return totaldays + day + 1 if is_leap_year(year) else totaldays + day
    elif month == 1:
        return day
    elif month == 2:
        return 31 + day
    else:
        return '输入有误'
print(which_day(2004, 12,7))

print('PRACTICE6: 约瑟夫环问题--------------')
def luckyloop():
    persons = [True] * 30
    """
    counter：被丢下海的人数
    index: 数到第几个人
    number: 9报数循环
    """
    counter, index, number = 0, 0, 0
    while counter < 15:
        if persons[index]:
            number += 1
            if number == 9:
                persons[index] = False
                number = 0
                counter += 1
        index += 1
        index %= 30
    for person in persons:
        print('基' if person else '非', end=' ')
    print()
luckyloop()
