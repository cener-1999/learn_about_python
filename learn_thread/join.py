#使用join()的例子 
import threading
import time

def context(tJoin):
    print ('in threadContext')
    tJoin.start()
    
    #将阻塞tContext直到threadJoin终止
    tJoin.join()
    print ('out threadContext')
    
    #tJoin终止后继续执行
    
def join():
    print('In threadJoin.')
    time.sleep(1)
    print('out threadJoin.')

#创建一个线程，线程里执行join函数
tJoin = threading.Thread(target=join)
#创建一个线程，线程里开始子线程
tContext=threading.Thread(target=context,args=(tJoin,))

tContext.start()