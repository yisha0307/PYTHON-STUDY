# 文件和异常
def readFile():
    f = None
    try:
        f = open('致橡树.txt', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件！')
    except LookupError:
        print('指定了未知的编码')
    except UnicodeDecodeError:
        print('读取文件时解码错误！')
    finally:
        if f:
            f.close()
readFile()

def readF():
    # with指定文件对象的上下文环境并在离开上下文环境时自动释放文件资源
    # 不用写finally因为with会自动关掉
    try:
        with open('致橡树.txt', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件！')
    except LookupError:
        print('指定了未知的编码')
    except UnicodeDecodeError:
        print('读取文件时解码错误！')
readF()

import time
def readText():
    with open('致橡树.txt', mode='r') as f:
        for line in f:
            print(line, end=' ')
            time.sleep(0.5)
        '''
        lines = f.readlines()
        '''
    print()

print('-------------将文本信息写入文件------------')
from math import sqrt
def is_prime(n):
    # 判断是不是素数
    for factor in range(2, int(sqrt(n))+1):
        if n % factor == 0:
            return False
        return True if n != 1 else False

def whitePrimes():
    filenames = ('a.txt', 'b.txt', 'c.txt')
    fs_list = []
    try:
        for filename in filenames:
            fs_list.append(open(filename, 'w', encoding = 'utf-8'))
        for number in range(1, 10000):
            if is_prime(number):
                if number < 100:
                    fs_list[0].write(str(number) + '\n')
                elif number < 1000:
                    fs_list[1].write(str(number) + '\n')
                else:
                    fs_list[2].write(str(number) + '\n')
    except IOError as e:
        print(e)
        print('写文件时发生错误！')
    finally:
        for fs in fs_list:
            fs.close()
    print('操作完成')

def readImg():
    try:
        with open('guido.jpg', 'rb') as fs1:
            data = fs1.read()
            print(type(data))
        with open('jiduo.jpg', 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as er:
        print(er, '指定的文件无法打开.')
    except IOError as e:
        print(e, '读写文件时出现错误.')
    print('程序执行完毕.')



import json
def writeDict():
    mydict = {
        'name': '骆昊',
        'age': 38,
        'qq': 957658,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open('data.json', 'w', encoding='utf-8') as f:
            # 写入json
            json.dump(mydict, f)
    except IOError as e:
        print(e)
    print('保存数据完成！')
writeDict()

import requests
import json

def request():
    resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
    data_model = json.loads(resp.text)
    for news in data_model['newslist']:
        print(news['title'])
