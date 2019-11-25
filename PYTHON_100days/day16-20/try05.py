'''
迭代器和生成器
'''
def fib(num):
    a,b = 0,1
    for _ in range(num):
        a, b = b, a+b
        yield a
class Fib(object):
    # 迭代器
    def __init__(self,num):
        self.num = num
        self.a, self.b = 0,1
        self.idx = 0

    def __iter__(self):
        return self
    def __next__(self):
        if self.idx < self.num:
            self.a, self.b = self.b, self.a + self.b
            self.idx += 1
            return self.a
        raise StopIteration()
