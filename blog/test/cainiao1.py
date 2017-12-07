#有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
def exercisee1():
    num=0
    for i in range(1,5):
        for j in range(1,5):
            if i!=j:
                for k in range(1,5):
                    if k!=i and k!=j:
                        print(100*i+10*j+k)
                        num=num+1
    print(num)


exercisee1()