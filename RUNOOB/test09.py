print([str(round(355/113, i)) for i in range(1, 6)])

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
# 以下两个式子等价
result = [[row[i] for row in matrix] for i in range(4)]
print(result)

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)

dictt = dict([('sape', 4139), ('guido', 4127), ('jack', 4040)])
print(dictt)

dicttt = dict(sape = 4156, jack = 7070, rose= 5023)
print(dicttt)

# 字典遍历时，关键字和对应的值可以使用items()解读出来
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k,v in knights.items():
    print(k, v)
# 在序列遍历时，索引位置和对应值可以用enumerate()函数同时得到
for i,v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q,a in zip(questions, answers):
    # 以下三个是等价的 f-string是3.6之后的
    print('What is your {0}?  It is {1}.'.format(q,a))
    print('What is your %s?  It is %s.'% (q,a))
    print(f'What is your {q}?  It is {a}.')

print(dir())

# for x in range(1, 11):
#     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
#     print(repr(x*x*x).rjust(4))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

# 在:后传入一个整数，可以保证该域至少有这么多的宽度
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
for name, number in table.items():
    print('{0:10} ==> {1:10d}'.format(name, number))

print('Runoob: {Runoob:d}; Google: {Google:d}; Taobao: {Taobao:d}'.format(**table))