listt = [3,45,67,5,70,29,5002]
# 排序算法
'''
--------简单选择排序----------
在要排序的一组数中，选出最小（或者最大）的一个数与第1个位置的数交换；
然后在剩下的数中再找最小（或者最大）的与第2个位置的数交换，
以此类推，知道第n-1个元素（倒数第二个数）和第n个元素（最后一个数）
比较为止。
'''
def select_sort(original_items, comp=lambda x,y: x<y):
    items = original_items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i+1, len(items)):
            if (comp(items[j], items[min_index])):
                min_index = j
        items[i], items[min_index] =items[min_index], items[i]
    return items
# print(select_sort(listt))

'''
------------冒泡排序------------
它重复地走访过要排序的元素列，依次比较两个相邻的元素，
如果顺序（如从大到小、首字母从从Z到A）错误就把他们交换过来。
'''
# def bubble_sort(items, comp = lambda x,y : x<y):
#     items = items[:]
#     for i in range(len(items) - 1):
#         for j in range(len(items) - 1 - i):
#             if (comp(items[j+1], items[j])):
#                 items[j+1], items[j] = items[j], items[j+1]
#     return items
def bubble_sort(original_items, comp = lambda x,y: x<y):
    items = original_items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(len(items) - 1 -i):
            if comp(items[j+1], items[j]):
                items[j+1], items[j] = items[j], items[j+1]
                swapped = True
        if not swapped:
            # 如果在排序的过程中没有数字变动位置，就证明已经是有序的了，不需要再排
            break
        return items
# print(bubble_sort(listt))

'''
归并排序
属于递归的一种排序
'''
def merge_sort(items, comp = lambda x,y: x<y):
    if len(items) < 2:
        return items[:]
    mid = len(items) // 2
    left = merge_sort(items[:mid], comp)
    right = merge_sort(items[mid:], comp)
    return merge(left, right, comp)

def merge(item1, item2, comp):
    items = []
    index1, index2 = 0, 0
    while index1 < len(item1) and index2 < len(item2):
        if comp(item1[index1], item2[index2]):
            items.append(item1[index1])
            index1 += 1
        else:
            items.append(item2[index2])
            index2 += 1 
    items += item1[index1:]
    items += item2[index2:]
    return items
print(merge_sort(listt))

'''
顺序查找
'''
def seq_search(items, key):
    # return 出现的第一个指定key的index
    for index, item in enumerate(items):
        if item == key:
            return index
    return -1

'''
折半查找
'''
def bin_search(items, key):
    start, end = 0, len(items) -1
    while start <= end:
        mid = (start + end ) // 2
        if key > items[mid]:
            start = mid + 1
        elif key < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1



'''
使用生成式（推导式）语法
'''
prices = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}
# 用股票价格大于100元的股票构造一个新的字典
prices2 = {key:value for key, value in prices.items() if value > 200}
print('price2', prices2)

# names = ['关羽', '张飞', '赵云', '马超', '黄忠']
# courses = ['语文', '数学', '英语']

# scores = [[None] * len(courses) for _ in range(len(names))]
# for row, name in enumerate(names):
#     for col, course in enumerate(courses):
#         scores[row][col] = float(input('请输入{}的{}成绩'.format(name, course)))
# print(scores)


"""
heapq
从列表中找出最大的或最小的N个元素
堆结构(大根堆/小根堆)
"""
import heapq

list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
list2 = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
# print(heapq.nlargest(3, list1))
# print(heapq.nsmallest(3, list1))
# print(heapq.nlargest(2, list2, key=lambda x: x['price']))
# print(heapq.nsmallest(4, list2, key = lambda x: x['shares']))

'''
穷举法例子:
公鸡5元一只 母鸡3元一只 小鸡1元三只
用100元买100只鸡 问公鸡/母鸡/小鸡各多少只
'''
for x in range(20):
    for y in range(33):
        z = 100 - x - y
        if (5*x+3*y+z//3 == 100 and z%3 == 0):
            print(x,y,z)

# A、B、C、D、E五人在某天夜里合伙捕鱼 最后疲惫不堪各自睡觉
# 第二天A第一个醒来 他将鱼分为5份 扔掉多余的1条 拿走自己的一份
# B第二个醒来 也将鱼分为5份 扔掉多余的1条 拿走自己的一份
# 然后C、D、E依次醒来也按同样的方式分鱼 问他们至少捕了多少条鱼
fish = 6
while True:
    total = fish
    enough = True
    for _ in range(5):
        if (total -1) % 5 == 0:
            total = (total-1) //5 * 4
        else:
            enough = False
            break
    if enough:
        print(fish)
        break
    fish += 5
    
'''
贪婪法例子:
'''
class Thing(object):
    def __init__(self, name, price, weight):
        self._name = name
        self._price = price
        self._weight = weight
    @property
    def value(self):
        # 价格重量比
        return self._price/self._weight

def input_things():
    # 输入物品信息
    name_str, price_str, weight_str = input().split()
    return name_str, int(price_str), int(weight_str)
    
def thiefValue():
    max_weight, num_of_things = map(int, input().split())
    all_things = []
    for _ in range(num_of_things):
        all_things.append(Thing(*input_things()))
    # 按照value进行排序
    all_things.sort(key=lambda x: x.value, reverse=True)
    total_weight = 0
    total_price = 0
    for thing in all_things:
        if total_weight + thing._weight <= max_weight:
            print(f'小偷拿走了{thing.name}')
            total_weight += thing._weight
            total_price += thing._price
    print(f'总价值: {total_price}美元')
thiefValue()