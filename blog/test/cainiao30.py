#一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
def exercise30(num):
    wan = (num // 10000)
    qian = (num // 1000)-wan*10
    bai = (num // 100)-wan*100-qian*10
    shi = (num // 10)-wan*1000-qian*100-bai*10
    ge = num-wan*10000-qian*1000-bai*100-shi*10
    print(wan,qian,bai,shi,ge)
    if wan==ge and shi==qian:
        print('是回文数')
    else:
        print('不是回文数')

exercise30(18321)

