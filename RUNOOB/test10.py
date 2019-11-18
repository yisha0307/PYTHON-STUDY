# str = input("请输入: ")
# print("你输入的内容是： ", str)

# 写入数据
# f = open('./foo.txt', 'w')
# f.write("Python是一个非常好的语言\n是的，的确非常好！\n")

# f.close()

# 读取文件
# f = open('./foo.txt', 'r')
# str = f.readlines()
# print(str)
# f.close()

# 不是字符串的东西要先进行转换
# f = open('./foo.txt', 'w')
# value = ('www.runoob.com', 14)
# s = str(value)
# f.write(s)
# f.close()

import pprint, pickle
# 使用Pickle模块将数据对象保存到文件
data1 = {'a': [1, 2.0, 3, 4+6j],
        'b': ('string', u'Unicode string'),
        'c': None}
selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open('data.pkl', 'wb')
pickle.dump(data1, output)
pickle.dump(selfref_list, output, -1)

output.close()
# 使用pickle模块从文件中重构python对象
pkl_file = open('data.pkl', 'rb')
data3 = pickle.load(pkl_file)
pprint.pprint(data3)
data4 = pickle.load(pkl_file)
pprint.pprint(data4)
pkl_file.close()