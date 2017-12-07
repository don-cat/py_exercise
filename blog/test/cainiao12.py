#   判断101-200之间有多少个素数，并输出所有素数。

from math import sqrt
def exercise12():
    for num in range(101,201):
        flag = True
        for j in range(2,int(sqrt(num))):
            if num%j==0:
                flag = False

        if flag == True:
            print(num)

exercise12()