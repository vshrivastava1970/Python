def add():
    a = 10
    b = 20
    print(a + b)


def sub():
    a = 20
    b = 10
    print(a - b)


add()
sub()

# #################
import threading


class MyThread(threading.Thread):
    def __init__(self, f):
        self.func = f
        super().__init__()

    def run(self):
        print('Inside Run')
        mylock.acquire()
        self.func()
        print('EOT: End of Row')
        mylock.release()


# ###### For Thread Locking #
mylock = threading.Lock()

t1 = MyThread(add)
t2 = MyThread(sub)

t1.start()
t2.start()
t2.join()
print(threading.active_count())
# print(threading.enumerate())

# Priorty Queue
import queue

q = queue.Queue(4)
t3 = MyThread(add)
t4 = MyThread(sub)

q.put(t3)
q.put(t4)
print(q.empty())
print(q.qsize())
print(q.full())

while not q.empty():
    t = q.get()
    t.start()
    t.join()
