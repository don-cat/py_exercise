#求1+2!+3!+...+20!的和。
def exercise25():
    sum = 0
    for i in range(1,21):
        ji = 1
        for j in range(1,i+1):
            ji = ji*j
        sum = sum+ji
    print(sum)

# exercise25()

def exercise25_2():
    sum = 0
    ji = 1
    for i in range(1,21):
        ji = ji*i
        sum = sum + ji
    print(sum)

# exercise25_2()

def exercise25_3():
    def op(n):
        sum = 1
        for i in range(1,n+1):
            sum = sum * i
        return sum

    l = range(1,21)
    ji = sum(map(op,l))
    print(ji)

exercise25_3()