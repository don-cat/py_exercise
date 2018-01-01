#multiprocessing exercise
import os
from multiprocessing import Process
def multiprocessing_exercise():
    print("this is process:%s"% os.getpid())
    print("process end %s"% os.getpid())

if __name__ == "__main__":
    p = Process(target=multiprocessing_exercise,)
    print("进程已初始化")
    p.start()
    p.join()
    print("process end %s"% os.getpid())