from multiprocessing import Process, Queue
from time import sleep

def producer(q):
    for i in range(1,6):
        print("Produced:", i)
        q.put(i)
        sleep(1)

def consumer(q):
    for i in range(1,6):
        item = q.get()
        print("Consumed:", item)

if __name__ == "__main__":

    q = Queue()

    p1 = Process(target=producer,args=(q,))
    p2 = Process(target=consumer,args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()