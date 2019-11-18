# python3
x = 'a'
y = 'b'
print(x)
print(y)

print('-----------')
# 不换行输出 要在变量末尾加上end=' ', 中间要有空格
print(x, end=' ')
print(y, end=' ')
print()

print(x,y)

# 导入sys模块
import sys
print('=========python import mode======')
print('命令行参数为:')
for i in sys.argv:
    print(i)
print('\n python路径为', sys.path)

# 导入sys模块的argv, path成员
from sys import argv, path
print("========python from import========")
print('path: ', path)

a = set('anjsbsfad')
b = set('jsadasdm')

print(a)
# 差集 (a有b没有)
print(a-b)
# 并集
print(a|b) 
# 交集
print(a&b)
# 不同时存在的元素 (要么a有要么b有)
print(a^b)

'''
这是多行注释
这是多行注释
'''
"""
这也是多行注释
这也是多行注释
"""