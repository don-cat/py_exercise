#古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？#实际是斐波那契数列
def exercise11(month):
    l = [0, 1]

    if month == 0:
        l = [0]
    elif month == 1:
        l = [0, 1]
    else:
        for i in range(2, month - 1):
            l.append(l[i - 2] + l[i - 1])

    print(l)


exercise11(14)
