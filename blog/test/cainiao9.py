#暂停一秒输出.

import time


def exercise9():
    print(time.ctime())
    time.sleep(1)
    print(time.ctime())

exercise9()