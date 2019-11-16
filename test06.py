# -*- coding: UTF-8 -*-

# dict类型
dict = {'name': 'runoob', 'age': 7, 'class': 'first'}
dict['age'] = 8
print(dict)

dict = {'Name': 'Runoob', 'Age': 7, 'Name': '小菜鸟'}
print(dict)

# set类型
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print('orange' in basket)
print('crabgrass' in basket)

thisset = set(('google', 'runoob', 'taobao'))
thisset.add('facebook')
print(thisset)

thisset.update({1,3})
print(thisset)