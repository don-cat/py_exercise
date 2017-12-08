#将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
def exercise14(num):
    if num!=1:
        for i in range(2,int(num+1)):
            if num%i==0:
                print(i)
                exercise14(int(num/i))
                return

exercise14(90)