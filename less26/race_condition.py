from threading import Thread, Lock
from time import sleep

counter = 0


def increase(by):
    global counter

    local_counter = counter
    local_counter += by

    sleep(0.1)

    counter = local_counter
    print(f'{counter=}')


t1 = Thread(target=increase, args=(10,))
t2 = Thread(target=increase, args=(20,))

t1.start()
t2.start()

t1.join()
t2.join()

# Используем lock

counter = 0


def increase(by, lock: Lock):
    global counter

    lock.acquire()

    local_counter = counter
    local_counter += by

    sleep(0.1)

    counter = local_counter
    print(f'{counter=}')

    lock.release()


lock = Lock()

t1 = Thread(target=increase, args=(10, lock))
t2 = Thread(target=increase, args=(20, lock))

t1.start()
t2.start()

t1.join()
t2.join()
