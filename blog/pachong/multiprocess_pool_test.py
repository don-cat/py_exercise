import os,time
from multiprocessing import Pool
def multiprocessing_exercise(i):
    print("this is process:%s,num:%s"% (os.getpid(),i))
    print("process end %s,num:%s"% (os.getpid(),i))

if __name__ == "__main__":
    pool = Pool(5)
    print("进程初始化")
    for i in range(6):
        try:
            pool.apply_async(multiprocessing_exercise,args=(i,))
        except Exception as e:
            print(e)
        # pool.apply(multiprocessing_exercise,args=(i))
    pool.close()
    time.sleep(10)
    pool.join()
    print("process end %s"% os.getpid())