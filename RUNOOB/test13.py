# 作用域
num = 1
def fun1 ():
    global num # global内部修改外部作用域的变量
    print(num)
    num = 123
    print(num)

fun1()
print(num)

# 修改嵌套作用域enclosing作用域而非全局作用域： nonlocal
def outer():
    num = 10
    def inner():
        nonlocal num
        num = 100
        print(num)
    inner()
    print(num)
outer()