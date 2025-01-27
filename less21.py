'''Создайте функцию для отображения текущего времени.
Функция не принимает параметров. Функция не используя синтаксис декораторов, произведите декорирование
функции с помощью другой функции. Потенциальный
вывод данных на экран:
***************************
23:00
***************************
В этом выводе на экран две линии из звездочек – результаты декорирования.'''
import time


def show_time():
    print(time.strftime('%H:%M'))


show_time()
print('')


def decorator_for_show_time(func):
    def new_func():
        print("*" * 20)
        func()
        print("*" * 20)

    return new_func


decorator_for_show_time(show_time)()
print('')
'''Задание 2
Добавьте ещё одну функцию для декорирования вывода
данных. Эта функция должна добавить новые элементы
в форматирование вывода.'''


def add_title_for_show_time(func):
    def new_func():
        print("Current time: ", end='')
        func()

    return new_func


decorator_for_show_time(add_title_for_show_time(show_time))()
print('')
'''Задание 3
Решите задачу из первого задания с использованием
синтаксиса декораторов.'''


def time_decorator(func):
    def wrapper():
        print('*' * 20)
        func()
        print('*' * 20)

    return wrapper


@time_decorator
def show_time():
    print(time.strftime('%H:%M'))


show_time()

'''Задание 4
Создайте приложение по выпечке пиццы. Каждая
пицца содержит разные компоненты. Используя механизм
декораторов создайте разные пиццы:
■ Маргарита;
■ Четыре сыра;
■ Капричоза;
■ Гавайская.'''


def margarita_decorator(func):
    def wrapper():
        print("Маргарита: ", end='')
        func()
        print('и добавим сыр Маргарита')
    return wrapper

def four_cheese_decorator(func):
    def wrapper():
        print("Пицца 4 сыра: ", end='')
        func()
        print('и добавим 4 сыра')
    return wrapper


def hawaiian_decorator(func):
    def wrapper():
        print("Гавайская пицца: ", end='')
        func()
        print('и добавим ананасы с курицей')
    return wrapper


@four_cheese_decorator
def create_pizza():
    print("Лепешка + томатный соус")


create_pizza()
