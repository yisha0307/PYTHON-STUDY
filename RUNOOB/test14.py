# 求和
print('1-------------')
def sum(*vattuple):
    total = 0
    for i in vattuple:
        try:
            total += i
        except TypeError:
            print(i, "不是数字")
            continue
    return total

print(sum(4,5,'6',8))

# 平方根
print('2-------------')
def sqrt(num):
    try:
        result = num ** 0.5
    except TypeError:
        print('请输入数字')
    else:
        print('{0}的平方根是{1:0.4f}'.format(num, result))
sqrt(202020)

# 计算三角形的面积
print('3-------------')
def triarea(a,b,c):
    s = (a + b + c) / 2
    area = (s*(s-a)*(s-b)*(s-c))**0.5
    print('三角形的面积是{0:0.3f}'.format(area))
triarea(10, 12, 14)

# 计算圆的面积
print('4--------------')
