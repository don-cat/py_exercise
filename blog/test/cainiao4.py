#输入某年某月某日，判断这一天是这一年的第几天？
def exercise4():
    year=int(input("year:"))
    month=int(input("month:"))
    day=int(input("day:"))
    days = 0

    if (year%4==0 and year%100!=0) or year%400==0:
        monday = [31,29,31,30,31,30,31,31,30,31,30,31]
    else:
        monday = [31,28,31,30,31,30,31,31,30,31,30,31]

    for i in range(0,month-1):
        print(monday[i])
        days = days+monday[i]


    days = days+day
    print(days)
exercise4()