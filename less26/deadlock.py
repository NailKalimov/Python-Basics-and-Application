import time
from threading import Thread, Lock

a_lock = Lock()
b_lock = Lock()


def func_a():
    a_lock.acquire()
    print("поток 1. Произведена Блокировка А")
    time.sleep(1)
    print("поток 1. Производится попытка получить блокировку B")
    b_lock.acquire()

    print("Все блокировки получены, выполняется поток 1")

    b_lock.release()
    a_lock.release()


def func_b():
    b_lock.acquire()
    print("поток 2. Произведена Блокировка B, ожидание блокировки A")
    a_lock.acquire()

    print("Все блокировки получены, выполняется поток 2")

    a_lock.release()
    b_lock.release()


thread_a = Thread(target=func_a)
thread_b = Thread(target=func_b)

thread_a.start()
thread_b.start()
thread_a.join()
thread_b.join()
