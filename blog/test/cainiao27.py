#利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
def exercise27():
    word = input('输入字符:\n')
    print_last_word(word)

def print_last_word(word):
    print(word[-1],end='')
    if len(word)>1:
        print_last_word(word[:-1])

exercise27()