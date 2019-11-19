# 面向对象编程

class Student(object):
    # __init__是一个特殊方法用在创建对象时进行初始化操作
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def study(self, course_name):
        print('%s正在学习%s' % (self.name, course_name))

print('--------练习1：定义一个类描述数字时钟--------')
from time import sleep
class Clock(object):
    def __init__(self, hour=0, minute = 0, second = 0):
        '''
        初始化方法
        :param hour: 时
        :param minute: 分钟
        :param second: 秒
        '''
        self._hour = hour
        self._minute = minute
        self._second = second
    def run(self):
        '''走字'''
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._hour += 1
                self._minute =0
                if self._hour == 24:
                    self._hour = 0
    def show(self):
        return ('%02d:%02d:%02d' % (self._hour, self._minute, self._second))

def main():
    clock = Clock(23, 59, 58)
    while True:
        print(clock.show())
        sleep(1)
        clock.run()
if __name__ == '__main__':
    main()