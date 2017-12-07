#输出 9*9 乘法口诀表。
def exercise8():
    for i in range(1,10):
        print()
        for j in range(1,i+1):
            print("%s * %s = %s" % (i,j,i*j),end=' ')

exercise8()