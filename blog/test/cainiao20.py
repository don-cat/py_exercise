#一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
def exercise20(num):
    sum = 100
    high = 50
    for i in range(num):
        sum = sum + high*2
        high = high/2

    print(sum)

exercise20(9)