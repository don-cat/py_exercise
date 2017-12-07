#暂停一秒输出，并格式化当前时间。

import time


def exercise10():
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    time.sleep(1)
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

exercise10()