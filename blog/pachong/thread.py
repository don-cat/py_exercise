import os
from multiprocessing import Process
def run_proc(name):
    print('chil process %s(%s） running' % (name,os.getpid()))

if __name__ == '__main__':
    print('parent process %s' % os.getpid())
    for i in range(50):
        p = Process(target=run_proc,args=(str(i),))
        print('process will start')
        p.start()
    p.join()
    print('Process end')