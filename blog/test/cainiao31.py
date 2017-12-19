#请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
def exercise31():
    shouzimu = ['M','T','W','T','F','S','S']
    xingqi = ['1','2','3','4','5','6','7']
    shou = input('请输入首字母:\n')
    for i in range(len(shouzimu)):
        if shou == shouzimu[i]:
            if shou == 'T':
                er = input('请输入第二个字母:\n')
                if er=='u':
                    print('2')
                else:
                    print('4')
            if shou == 'S':
                er = input('请输入第二个字母:\n')
                if er=='a':
                    print('6')
                else:
                    print('7')
        else:
            print(xingqi[i])

exercise31()