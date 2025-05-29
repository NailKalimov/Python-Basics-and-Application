"""
В Python атомарной операцией является строчка байткода, который исполняет интерпретатор
между этими строчками теоретически может произойти переключение GIL
Проверить, в какой байт код компилируется наша программа можно с помощью dis.dis()
"""

import dis
a=[]
def inc(a):
    a+=1
    return a

def add():
    a.append(1)

print(dis.dis(inc)) # 4 команды
print(dis.dis(add)) # 5 команд, но по документации это атомарная операция

"""
Пример, доказывающий неатомарность инкрементирования
"""
# from concurrent.futures import ThreadPoolExecutor, wait
# import sys
# from threading import Thread
# import time

# sum = 0
# sys.setswitchinterval(0.000001)
# def inc():
#     time.sleep(0.01)
#     global sum
#     sum += 1
#     # for _ in range(1000):
#     #     sum += 1

# # executor = ThreadPoolExecutor()
# # futures = [executor.submit(inc) for _ in range(2000)]
# # wait(futures)
# # executor.shutdown(wait=True)

# threads=[]
# for _ in range(2000):
#     threads.append(Thread(target=inc))
# for t in threads:
#     t.start()
# for t in threads:
#     t.join()
# print(sum)