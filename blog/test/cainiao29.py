#给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
def exercise29(num):
    n = 1
    for i in range(1,6):
        if num/n>10:
            y = int((num % (n*10))/n)
            n = n*10
            num = num-y
            print(y)
        else:
            y = int((num % (n * 10)) / n)
            n = n * 10
            print(y)
            print('是%s位数' % i)
            break

exercise29(546)

