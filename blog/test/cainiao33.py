#按逗号分隔列表
def exercise33():
    l = [1,2,3,4,5,8]
    s1 = ','.join(str(n) for n in l)# join():连接字符串数组。将字符串、元组、列表中的元素以指定的字符(分隔符)连接生成一个新的字符串
    print(s1)

exercise33()