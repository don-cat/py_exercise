#一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少?？
def exercise3():
   i = 1
   for i in range(1,int(168/2+1)):
       j=168/i
       if j%2==0 and i%2==0 and i>j:
               # print(i,j)
               m=(i+j)/2
               n=(i-j)/2
               print(m * m-268)
       elif j%1==0 and j%2!=0:
           if i%2!=0 and i%1==0 and i>j:
               # print(i, j)
               m = (i + j) / 2
               n = (i - j) / 2
               print(m * m - 268)

exercise3()