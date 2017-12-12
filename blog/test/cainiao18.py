#求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
def exercise18():
    num = int(input('输入个数:\n'))
    a = 2
    s = 0

    for i in range(num):
        s = s + (num-i)*a*10**i

    print(s)

exercise18()