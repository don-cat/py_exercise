#按相反的顺序输出列表的值。
def exercise32():
    l = [1,2,3,4,5,8]
    for i in range(1,len(l)+1):
        print(l[0-i])

exercise32()