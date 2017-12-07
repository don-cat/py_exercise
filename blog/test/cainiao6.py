#斐波那契数列。 斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。

def exercise6(num):
    l = [0,1]

    if num == 0:
        l = [0]
    elif num == 1:
        l = [0,1]
    else:
        for i in range(2,num-1):
            l.append(l[i-2]+l[i-1])

    print(l)

exercise6(10)
