from threading import Thread, Semaphore
from time import sleep

def display(str1):
    l.acquire()
    for x in str1:
        print(x)
        sleep(1)
    l.release()


l= Semaphore(2)
t1=Thread(target=display,args=('helo',))
t2=Thread(target=display,args=('welcome',))


t1.start()
t2.start()

t1.join()
t2.join()

