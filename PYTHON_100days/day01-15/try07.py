# 面向对象进阶
class Person(object):
    # 限定Person对象只能绑定_name, _age和_gender属性
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age
    # @property装饰器 - getter方法
    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age
    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self._age = age
    
    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)

def createPerson():
    person = Person('王大锤', 12)
    person.play()
    person.age = 22
    person.play()

createPerson()


from math import sqrt

class Triangle(object):
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
    # 静态方法
    @staticmethod
    def is_valid(a, b, c):
        return a+b>c and a+c>b and b+c>a
    def perimeter(self):
        return self._a + self._b + self._c
    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half-self._a) * (half - self._b) * (half - self._c))

def triang():
    a, b, c = 3, 4, 5
    if (Triangle.is_valid(a, b, c)):
        t = Triangle(a, b, c)
        print(t.perimeter())
        print(t.area())
    else:
        print('无法构成三角形')
triang()

'''数字时钟'''
from time import time, localtime, sleep
class Clock(object):
    def __init__(self, hour=0, minute=0, second =0):
        self._hour = hour
        self._minute = minute
        self._second = second
    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)
    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0
    def show(self):
        """显示时间"""
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade
    @property
    def grade(self):
        return self._grade
    @grade.setter
    def grade(self, grade):
        self._grade = grade
    def study(self, course):
        print('%s的%s正在学习%s.' % (self._grade, self._name, course))

stu = Student('王大锤', 15, '初三')
print(stu.grade)

print('***************案例1：奥特曼打小怪兽****************')

from abc import ABCMeta, abstractmethod
from random import randint, randrange

class Fighter(object, metaclass = ABCMeta):
    # 战斗者
    __slots__ = ('_name', '_hp')
    def __init__(self, name, hp):
        '''
        :param name: 名字
        :param hp: 生命值
        '''
        self._name = name
        self._hp = hp
    @property
    def name(self):
        return self._name
    @property
    def hp(self):
        return self._hp
    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0
    @property
    def alive(self):
        return self._hp > 0
    @abstractmethod
    # abstractmethod表示这个类不能被实例化
    def attack(self, other):
        pass
# 奥特曼
class Ultraman(Fighter):
    __slots__ = ('_name', '_hp', '_mp')
    def __init__(self, name, hp, mp):
        # :param mp: 魔法值
        super().__init__(name, hp)
        self._mp = mp
    def attack(self, other):
        other.hp -= randint(15, 25)
    def huge_attack(self, other):
        """
        究极必杀技(打掉对方至少50点或四分之三的血)

        :param other: 被攻击的对象

        :return: 使用成功返回True否则返回False
        """
        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp * 3 // 4
            injury = injury if injury >= 50 else 50
            other.hp -= injury
            return True
        else:
            self.attack(other)
            return False
    def magic_attack(self, others):
        """
        魔法攻击

        :param others: 被攻击的群体

        :return: 使用魔法成功返回True否则返回False
        """
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp.hp -= randint(10, 15)
            return True
        else:
            return False

    def resume(self):
        """恢复魔法值"""
        incr_point = randint(1, 10)
        self._mp += incr_point
        return incr_point
    def __str__(self):
        return '~~~%s奥特曼~~~\n' % self._name + \
            '生命值: %d\n' % self._hp + \
            '魔法值: %d\n' % self._mp
# 小怪兽
class Monster(Fighter):
    __slots__ = ('_name', '_hp')
    def attack(self, other):
        other.hp -= randint(10, 20)
    def __str__(self):
        return '~~~%s小怪兽~~~\n' % self._name + \
            '生命值: %d\n' % self._hp

def is_any_alive(monsters):
    # 判断有没有活着的小怪兽
    for any in monsters:
        if any.alive > 0:
            return True
    return False

def select_alive_one(monsters):
    # 选择一只活着的小怪兽
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.alive:
            return monster

def display_info(ultraman, monsters):
    # 显示奥特曼和小怪兽的信息
    print(ultraman)
    for any in monsters:
        print(any, end=' ')

def main():
    u = Ultraman('骆昊', 1000, 120)
    m1 = Monster('狄仁杰', 250)
    m2 = Monster('白元芳', 500)
    m3 = Monster('王大锤', 750)
    ms = [m1, m2, m3]
    fight_round = 1
    while u.alive and is_any_alive(ms):
        print('========第%02d回合========' % fight_round)
        m = select_alive_one(ms) # 选中一只小怪兽
        skill = randint(1, 10) # 通过随机数选择使用哪项功能
        if skill <= 6: # 普通攻击
            print('%s使用普通攻击打了%s.' % (u.name, m.name))
            u.attack(m)
            print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
        elif skill <=9: # 使用魔法攻击
            if u.magic_attack(ms):
                print('%s使用了魔法攻击.' % u.name)
            else:
                print('%s使用魔法攻击失败.' % u.name)
        else:
            if u.huge_attack(m):
                print('%s使用究极必杀技虐了%s.' % (u.name, m.name))
            else:
                print('%s使用普通攻击打了%s.' % (u.name, m.name))
                print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
        if m.alive > 0:
            print('%s回击了%s.' % (m.name, u.name))
            m.attack(u)
        display_info(u, ms)
        fight_round += 1
    print('\n========战斗结束!========\n')
    if u.alive > 0:
        print('%s奥特曼胜利!' % u.name)
    else:
        print('小怪兽胜利!')


if __name__ == '__main__':
    main()