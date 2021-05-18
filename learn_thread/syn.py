import threading
import time

class myThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.name=name
        self.counter=counter
        
    def run(self):
        print('start thread'+self.name)
        #获取锁
        threadLock.acquire()
        print_time(self,self.counter,3)
        #释放锁
        threadLock.release()

def print_time(ThreadName,delay,counter):
    while counter:
        time.sleep(delay)
        print('%s:%s' % (ThreadName,time.ctime(time.time())))
        counter-=1
        

threadLock=threading.Lock()
threads=[]

thread1=myThread(1,'firstThread',1)
thread2=myThread(2,'secondThead',2)

thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)

#for t in threads:
    #t.join()
#print('退出主线程')