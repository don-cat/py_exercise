#利用递归方法求5!。
def exercise26(n):
    if n == 1:
        ji = 1
    else:
        ji = n * exercise26(n-1)

    return ji

print(exercise26(5))