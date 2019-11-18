# 迭代器和生成器
list = [1, 2, 3, 4]
# iter()创建迭代器
it = iter(list)
# 输出迭代器的下一个元素
# for i in it:
#     print(i, end=' ')

# import sys
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()

# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
#     def __next__(self):
#         x = self.a
#         self.a += 1
#         return x
# myclass = MyNumbers()
# myiter = iter(myclass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 3
            return x
        else:
            raise StopIteration
myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)

# 生成器是一个返回迭代器的函数，只能用于迭代操作
# 生成器会用到yield
# yield和next搭配

# import sys
# def fibonacci(n):
#     a, b, counter = 0, 1, 0
#     while True:
#         if (counter > n):
#             return
#         yield a
#         a, b = b, a+b
#         counter += 1

# f = fibonacci(10) #f是一个迭代器

# while True:
#     try:
#         print(next(f))
#     except StopIteration:
#         sys.exit()

def printme(str, len):
    print(str, len)
    return

printme(len = 5, str='ddd')

# def printinfo(name, age = 55):
#     print('名字: ', name)
#     print('年龄： ', age)
#     return
# printinfo(name = 'ruboon', age = 40)
# print('------------')
# printinfo(name = '666')

# 不定长参数
# 加了*的参数会以元组tuple的形式导入 存放所有未命名的变量参数
# 加了**的参数会以字典的形式导入
def printinfo(arg1, *vartuple):
    print("输出: ")
    print(arg1)
    for i in vartuple:
        print(i)
    return
printinfo(10)
printinfo(70, 60, 50)

def printinfo2 (arg1, **vardict):
    print("输出: ")
    print(arg1)
    print(vardict)

printinfo2(1, a=2, b=3)

# 匿名函数lambda
sum = lambda arg1, agr2: arg1 + agr2
print ("相加后的值为 : ", sum( 10, 20 ))

# return 语句
def sum1(arg1, arg2):
    total = arg1 + arg2
    print ("函数内 : ", total)
    return total

total = sum1(10, 20)
print ("函数外 : ", total)