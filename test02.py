# -*- coding: UTF-8 -*-
# python2
# s = 'hello world'
# print s[1:5]
# print s[0]
# print s[2:]
# print s * 2
# print s + 'TEST'
# print s[1:4:2]
# print s[0:4]
# print s[:4]

list = ['runoob', 789, 2.23, 'john', 70.2]
tinyList = [123, 'john']
print list
print list[0]
print list[1:3]
print list[2:]
print tinyList*2
print list + tinyList

# python 元组 相当于只读的list
tuple = ('runoob', 789, 2.23, 'john', 70.2)
tinytuple = (123, 'john')
print tuple
print tuple[0]
print tuple[1:3]
print tuple[2:]
print tinytuple * 2
print tuple + tinytuple

# 报错，因为元组不允许更新值
# tuple[2] = 1000

dict = {}
dict['one'] = 'This is one'
dict[2] = 'This is two'

tinyDict = {'name': 'john', 'code': 6734, 'dept': 'sales'}
print dict['one']
print dict[2]
print tinyDict
print tinyDict.keys()
print tinyDict.values()

a = 10
b = 20
llist = [10, 20, 3, 4, 5]
print (10 and 20)
print (10 or 20)
print not(10 and 20)
print (a not in llist)

a = [1, 2, 3]
b = a[:]
# is 判断是不是同一个存储空间
print b is a
# == 判断值是不是一样
print b == a