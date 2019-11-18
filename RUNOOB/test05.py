# -*- coding: UTF-8 -*-
print ("我叫 %s 今年 %d 岁" % ('小猫', 10))

para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB(\t).
也可以使用换行符[\n]。
"""
print(para_str)

# f-string
name = 'Runoob'
print (f'Hello {name}')

str = "[www.runoob.com]"
# center()
print("str.center(40, '*'): ", str.center(40, '*'))
# count()
print("str.count('o'): ", str.count('o'))
# encode() 和 decode()
newstr = '菜鸟教程'
str_utf8 = newstr.encode("UTF-8")
str_gbk = newstr.encode("GBK")
print(newstr)

print("UTF-8编码: ", str_utf8)
print("GBK编码: ", str_gbk)

print("UTF-8解码: ",str_utf8.decode('UTF-8', 'strict'))
print("GBK解码: ",str_gbk.decode('GBK', 'strict'))
# endswith()
Str = 'Runoob example ... wow!!!'
suffix = '!!'
print (Str.endswith(suffix))

list1= ['google', 'runoob', 'taobao']
list2 = list(range(5))
list1.extend(list2)
print('扩展后的列表: ', list1)