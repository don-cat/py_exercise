#输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
import string


def exercise17():
    s = input('input a string:\n')
    letters = 0
    space = 0
    num = 0
    other = 0
    for c in s:
        if c.isalpha():
            letters += 1
        elif c.isspace():
            space += 1
        elif c.isdigit():
            num += 1
        else:
            other += 1
    print('char = %d,space = %d,digit = %d,others = %d' % (letters, space, num, other))

exercise17()

