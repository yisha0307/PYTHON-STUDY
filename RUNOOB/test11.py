# 异常处理
# while True:
#     try:
#         x = int(input("请输入一个数字: "))
#         break
#     except ValueError:
#         print('您输入的不是数字，请再次尝试输入！')

# def this_fails():
#     x = 1/0
#     return x

# try:
#     this_fails()
# except ZeroDivisionError as err:
#     print('Handling run-time error: ', err)

# try:
#     runoob()
# except NameError as error:
#     print('------', error)
# else:
#     try:
#         with open('file.log') as file:
#             read_data = file.read()
#     except FileNotFoundError as fnf_error:
#         print(fnf_error)
# finally:
#     print('这句话，无论如何都会出现')

# print('-----------------')
# try:
#     raise NameError('HiThere')
# except NameError:
#     print('An exception flew by!')
#     raise

# 自定义异常
class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

try:
    raise MyError(2*2)
except MyError as e:
    print('My exception occured, value: ', e.value)

raise MyError('oops')