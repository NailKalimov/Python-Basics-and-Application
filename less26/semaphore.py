import time
from threading import Thread, Semaphore
import datetime

s = Semaphore(value=3)


def func(thread):
    s.acquire()
    now = datetime.datetime.now().strftime('%H:%M:%S')
    print(f'time: {now}, thread: {thread}')
    time.sleep(1)
    s.release()


threads = [Thread(target=func, args=(i,)) for i in range(1, 8)]

for t in threads:
    t.start()
for t in threads:
    t.join()
