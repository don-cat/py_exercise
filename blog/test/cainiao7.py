#将一个列表的数据复制到另一个列表中。
def exercise7_function1():
    list1 = [1,2,3,4,5,6,7,8,9,10]
    list2 = []
    for i in list1:
        print(i)
        list2.append(list1[i-1])
        print(list2)

def exercise7_function2():
    list1 = [1,2,3]
    b = [4,5,6]
    list2 = list1[:]
    print(list2)

exercise7_function2()