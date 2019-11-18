# -*- coding: UTF-8 -*-

# flag = False
# name = 'luren'
# if name == 'python':
#     flag = true
#     print 'welcome boss'
# else:
#     print name

# num = 5
# if num == 3:
#     print 'boss'
# elif num == 2:
#     print 'user'
# elif num == 1:
#     print 'worker'
# elif num < 0:
#     print 'error'
# else:
#     print 'roadman'

# numbers = [12, 37, 5, 43, 8 ,3]
# even = []
# odd = []
# while len(numbers) > 0 :
#     # 把最后的数字推出栈
#     number = numbers.pop()
#     if (number % 2 == 0):
#         even.append(number)
#     else:
#         odd.append(number)

# print even, odd

# count = 0
# while (count < 9):
#     print 'The count is:', count
#     count += 1
# print 'good bye'

# # continue和break的用法
# i = 1
# while i < 10:
#     i += 1
#     if i%2 > 0:
#         # continue 跳过该次循环
#         continue
#     print i

# i = 1
# while 1:
#     print i
#     i += 1
#     if i >10:
#         # break跳出循环
#         break

# count = 0
# while count < 5:
#     print count, " is less than 5"
#     count += 1
# else:
#     print count, " is not less than 5"

# for letter in 'Python':
#     print '当前字母:', letter
fruits = ['banana', 'apple', 'mango']
# for fruit in fruits:
#     print '当前水果：', fruit

# print "Good bye"

for index in range(len(fruits)):
    print ('当前水果:', fruits[index])
print ('-------------------')