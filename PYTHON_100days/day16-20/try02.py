listt = [3,45,67,5,70,29,5002]
'''
快速排序 - 选择枢轴对元素进行划分，左边都比枢轴小右边都比枢轴大
'''
def quick_sort(items, comp = lambda x,y:x<=y):
    items = items[:]
    _quick_sort(items, 0, len(items)-1, comp)
    return items

def _quick_sort(items, start, end, comp):
    if start < end:
        pos = _partition(items, start, end, comp)
        _quick_sort(items, start, pos-1, comp)
        _quick_sort(items, pos+1, end, comp)

def _partition(items, start, end, comp):
    # 选择主元
    pivot = items[end]
    i = start - 1
    for j in range(start, end):
        # 只要比主元小的数字就扔到前面（不需要排序）
        if comp(items[j], pivot):
            i += 1
            items[i], items[j] = items[j], items[i]
    items[i+1], items[end] = items[end], items[i+1]
    # return 最后主元的位置
    return i + 1

print(quick_sort(listt))

# 计算fibonacci数列
def fib(num):
    a, b = 1, 1
    result = [a, b]
    for _ in range(num):
        a, b = b, a+b
        result.append(b)
    return result

# 计算fibonacci数列上第num个数字是什么
def fib_num(num, temp={}):
    '''利用递归'''
    if num in (1, 2):
        # fibonacci的第一位和第二位上是1
        return 1
    try:
        return temp[num]
    except KeyError:
        temp[num] = fib_num(num - 1) + fib_num(num - 2)
        return temp[num]

print(fib_num(50))

# 动态规划例子2：子列表元素之和的最大值
def findMax():
    items = list(map(int, input().split()))
    size = len(items)
    overall, partial = {}, {}
    overall[size - 1] = partial[size - 1] = items[size - 1]
    for i in range(size-2, -1, -1):
        partial[i] = max(items[i], partial[i+1]+items[i])
        overall[i] = max(partial[i], overall[i+1])
    print(overall[0])
# findMax()

items1 = list(map(lambda x: x **2, filter(lambda x: x % 2, range(1, 10))))
items2 = [x ** 2 for x in range(1, 10) if x % 2]
print(items1, items2)

