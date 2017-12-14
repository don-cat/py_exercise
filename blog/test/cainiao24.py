#有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
def exercise24():
    sum  = 0
    fenzi = 2
    fenmu = 1
    for i in range(1,21):
        sum = sum +fenzi/fenmu
        t = fenzi
        fenzi = fenzi+fenmu
        fenmu = t
    print(sum)

exercise24()