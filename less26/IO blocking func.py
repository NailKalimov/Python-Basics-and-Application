"""
В данном примере видим, что функция ввода input() (аналогично time.sleep()) блокирует интерпретатор и
при этом освобождает GIL, что позволяет переключаться между процессами
"""

from threading import Thread


def func_IO():
    print("start func1")
    data = input("Ожидается ввод данных в функции 1\n")
    print(f"finish func1. Input data: {data}")

def func2():
    print("start func2")
    print("finish func2")

t1 = Thread(target=func_IO, daemon=True)
t2 = Thread(target=func2, daemon=True)

t1.start()
t2.start()
t1.join()
t2.join()