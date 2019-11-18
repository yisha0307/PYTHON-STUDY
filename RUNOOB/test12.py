# 面向对象编程
class MyClass:
    """一个简单的类实例"""
    i = 12345
    def f(self):
        return "hello world"

# 实例化类
x = MyClass()
print("MyClass类的属性i为: ", x.i)
print("MyClass类的方法f为: ", x.f())

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
x = Complex(3.0, -4.5)
print(x.r, x.i)

class Test:
    # 类的方法与普通函数的一点不同是，必须有一个额外的第一个参数名称，通常是self
    def prt(self):
        print(self)
        print(self.__class__)
t = Test()
t.prt()

class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性
    _weight = 0
    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self._weight = w
    def speak(self):
        print('{0}说: 我{1}岁，{2}公斤重'.format(self.name, self.age, self._weight))
# 继承
class student(people):
    grade = ''
    def __init__(self, n, a, w, g):
        # 调用父类的构造函数
        people.__init__(self, n, a, w)
        self.grade = g
    # 覆盖父类的方法
    def speak(self):
        print('{0}说: 我{1}岁，在读{2}年纪'.format(self.name, self.age, self.grade))

s = student('ken', 10, 60, 3)
s.speak()

class speak():
    topic = ''
    name = ''
    def __init__(self, n, t):
        self.name = n
        self.topic = t
    def speak(self):
        print('我叫 %s，我是一个演说家，我演讲的主题是 %s' % (self.name, self.topic))

# 多重继承
class sample(speak, student):
    a = ''
    def __init__(self, n, a, w, g, t):       
        speak.__init__(self, n, t)
        student.__init__(self, n,a,w,g)
test = sample('Tim', 25, 80, 4, 'Python')
# 方法名同，默认调用的在括号中排前的父类的方法
test.speak()

class Parent:
    def myMethod(self):
        print('调用父类方法')

class Child(Parent):
    def myMethod(self):
        print('调用子类方法')
c = Child()
# 子类调用重写方法
c.myMethod()
# 用子类对象调用父类已被覆盖的方法
super(Child, c).myMethod()
# or
# Parent().myMethod()

class Site:
    def __init__(self, name, url):
        self.name = name  #public
        self.url = url   #private
    def who(self):
        print('name :', self.name)
        print('url :', self.url)
    def __foo(self):   # 私有方法
        print('这是私有方法')
    def foo(self):
        print('这是公共方法')
        self.__foo()

x = Site('菜鸟教程', 'www.runoob.com')
x.who()
x.foo()
#x.__foo()  私有方法报错