#一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
def exercise19():
    for i in range(1000000001):
        s = 0
        for factor in range(1,i//2+1):
            if i%factor==0:
                s = s + factor
        if s==i:
            print(i)

exercise19()