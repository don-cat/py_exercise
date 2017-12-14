#打印出如下图案（菱形）:

#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

def exercise23():
    for i in range(1,8):
        if i<=4:
            x = int(2*i-1)
        if i>4:
            x = int((7-i)*2+1)
        k = abs(int((7-x)/2))
        for m in range(k):
            print(' ',end='')
        for n in range(x):
            print('*',end='')
        print('\n')


exercise23()