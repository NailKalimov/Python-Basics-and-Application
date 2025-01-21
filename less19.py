'''Какие числа будут выведены в результате выполнения данного кода?'''
class A:
    def __init__(self, val=0):
        self.val = val

    def add(self, x):
        self.val += x

    def print_val(self):
        print(self.val)


a = A()
b = A(2)
c = A(4)
a.add(2)
b.add(2)

a.print_val()
b.print_val()
c.print_val()


'''Какие числа будут выведены в результате выполнения данного кода?'''
class A:
    val = 1

    def foo(self):
        A.val += 2

    def bar(self):
        self.val += 1


a = A()
b = A()

a.bar()
a.foo()

c = A()

print(a.val)
print(b.val)
print(c.val)

'''Какие числа будут выведены в результате выполнения данного кода?'''
class Base:
    def __init__(self):
        print("- class Base init")
        self.val = 0

    def add_one(self):
        print("- class Base add_one")
        self.val += 1

    def add_many(self, x):
        print("- class Base add_many")
        for i in range(x):
            self.add_one()

class Derived(Base):
    #!!!
    def add_one(self):
        print("- class Derived add_one")
        self.val += 10

a = Derived()
a.add_one()
print("a =", a.val, "******")
b = Derived()
b.add_many(3)
print("b =", b.val, "******")

#######################
'''Одно из применений множественного наследование – расширение 
функциональности класса каким-то заранее определенным способом. 
Например, если нам понадобится логировать какую-то информацию при 
обращении к методам класса.

Рассмотрим класс Loggable:'''

import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))
'''У него есть ровно один метод log, который позволяет выводить в лог 
(в данном случае в stdout) какое-то сообщение, добавляя при этом текущее 
время.
Реализуйте класс LoggableList, отнаследовав его от классов list и 
Loggable таким образом, чтобы при добавлении элемента в список 
посредством метода append в лог отправлялось сообщение, состоящее из 
только что добавленного элемента.

Примечание
Ваша программа не должна содержать класс Loggable. При проверке вашей 
программе будет доступен этот класс, и он будет содержать метод log, 
описанный выше.'''

#answer:
'''class LoggableList(list, Loggable):
    def append(self, __object):
        # list.append(self, __object)
        super(LoggableList, self).append(__object)
        # Loggable.log(self, __object)
        super(LoggableList, self).log(__object)'''

#######################
class Descriptor:
    def __get__(self, obj, type):
        print("getter used")

    def __set__(self, obj, val):
        print("setter used")

    def __delete__(self, obj):
        print("deleter used")


class MyClass:
    prop = Descriptor()

# class MyClass:

#     def _getter(self):
#         print("getter used")
#     def _setter(self, val):
#         print("setter used")
#     def _deleter(self):
#         print("deleter used")

#     prop = property(_getter, _setter, _deleter, "doc string")


m = MyClass()
m.prop          # getter used
m.prop = 1      # setter used
del (m.prop)     # deleter used

##########################

# https://education.yandex.ru/handbook/python/article/volshebnye-metody-pereopredelenie-metodov-nasledovanie