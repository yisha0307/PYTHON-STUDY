print('1-------------------')
x = float(input('x= '))
if x > 1:
    y = 3 * x - 5
elif x > -1:
    y = x + 2
else:
    y = 5 * x + 3
print('f({x:0.2f}) = {y:0.2f}'.format(x=x,y=y))

print('2-------------------')
value = float(input('请输入长度: '))
unit = input('请输入单位: ')
if unit == 'in' or unit == '英寸':
    print('%.4f英寸 = %.4f厘米' % (value, value * 2.54))
elif unit == 'cm' or unit == '厘米':
    print('%.4f厘米 = %.4f英寸' % (value, value / 2.54))
else:
    print('请输入有效单位')

print('3------------')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    print('周长等于{0}'.format(a+b+c))
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print('面积等于{0}'.format(area))
else:
    print('不能构成三角形')