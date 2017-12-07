#输入三个整数x,y,z，请把这三个数由小到大输出。
def exercise5_function1():
    a = int(input("1:"))
    b = int(input("2:"))
    c = int(input("3:"))

    if a<b:
        if a<c and b<c:
            print(a,b,c)
        elif a<c:
            print(a,c,b)
        else:
            print(c,a,b)
    else:
        if b<c and c<a:
            print(b,c,a)
        elif b<c:
            print(b,a,c)
        else:
            print(c,b,a)

def exercise5_function2():
    l = []
    for i in range(0,3):
        a = int(input(i))
        l.append(a)

    l.sort()
    print(l)

# exercise5_function1()
exercise5_function2()
