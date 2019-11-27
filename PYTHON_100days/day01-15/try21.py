list = ['2', '3', '4']
numberlist = [int(x) for x in list]

def sum(list):
    total = 0
    for x in list:
        total += x
    return total

print(sum(numberlist))
