import os
from multiprocessing import Pool
def multiprocessing_exercise(i):
    print("this is process:%s,num:%s"% (os.getpid(),i))
    print("process end %s,num:%s"% (os.getpid(),i))

if __name__ == "__main__":
    pool = Pool(processes=5)
    print("进程初始化")
    for i in range(50):
        pool.apply_async(multiprocessing_exercise,args=(i))
    pool.close()
    pool.join()
    print("process end %s"% os.getpid())