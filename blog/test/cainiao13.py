#打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
def exercise13():
    num = range(0,9)
    num_list = list(map(lifang,num))
    for i in range(1,9):
        for j in range(0,9):
            for k in range(0,9):
                if num_list[i] + num_list[j] + num_list[k] == (100*i+10*j+k):
                    print(100*i+10*j+k)

def lifang(x):
    return x*x*x

exercise13()