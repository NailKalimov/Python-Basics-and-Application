"""Задание 1
Написать в словесной форме и нарисовать блок-схему
алгоритма посещения кинотеатра.
Задание 2
Написать в словесной форме и нарисовать блок-схему
алгоритма игры в боулинг.
Задание 3
Написать в словесной форме и нарисовать блок-схему
алгоритма езды на велосипеде.
Задание 4
Написать в словесной форме и нарисовать блок-схему
алгоритма покупки игровой приставки."""

"""Чтобы загрузить установщики для операционных систем Windows и Mac OS, достаточно перейти по ссылке
https://www.python.org/downloads/release/python-351/ ﻿и в самом низу страницы ﻿выбрать ﻿нужный
для вашей архитектуры установщик интерпретатора: для windows 64bit - "﻿Windows x86-64 executable installer",
для windows 32bit - "Windows x86 executable installer﻿", для Mac OS ﻿64 bit ﻿- ﻿"Mac
OS X 64-bit/32-bit installer", ﻿ для Mac OS 32bit/PPC - ﻿﻿"Mac OS X 32-bit i386/PPC installer".

Для того, чтобы установить python3 на операционных системах linux, необходимо ﻿использовать стандартные
﻿менеджеры пакетов﻿ ﻿(apt-get или yum) вашей операционной системы. Например, чтобы установить python3
на операционной системе ubuntu необходимо запустить в терминале следующую команду:

sudo apt-get install python3
Чтобы убедиться в том, что вы установили интерпретатор, необходимо запустить интерпретатор в терминале с помощью команды.

﻿python3"""

##############################
print("Hello, world!")

print("Hello,", "world!")

print("Hello", "world", sep=", ")

print("First row")
print("Second row")

print("First row", end=" ")
print("Second row")


input("Please enter something: ")

name = input("Enter your name: ")
print("My name is: ", name)


name = "Alice"
age = 25
print(name, age)  # Output: Alice 25

name, age = "Alice", 25
print(name, age)  # Output: Alice 25

name = "Alice"
other_name = name
print(other_name, name)  # Output: Alice Alice

x = 3
y = 4
print(x, y)  # Output: 3 4
x, y = y, x
print(x, y)  # Output: 4 3

variable = 1
print(type(variable))  # Output: <class 'int'>
variable = "Hello, world!"
print(type(variable))  # Output: <class 'str'>

# don't do this
print = 1
print(1)  # Output: TypeError: 'int' object is not callable


x = 10
y = 5
summary = x + y
print(summary)  # Output: 15

x = 10.5
y = 5.5
summary = x + y
print(summary)  # Output: 16.0

x = 10
y = 5
z = x * y
print(z)  # Output: 50

x = 10
y = 5
z = x / y
print(z)  # Output: 2.0

x = 10
y = 0
z = x / y
print(z)  # Output: ZeroDivisionError: division by zero

first_integer = 10
second_integer = 5
summary = first_integer + second_integer
print(summary)

x = 2
print(x ** 3)  # Output: 8

x = 9
y = 4
print(x // y)  # Output: 2
print(x % y)  # Output: 1

integer = 2 + 3 * 5
print(integer)  # Output: 17

integer = (2 + 3) * 5
print(integer)  # Output: 25

my_integer = 10
my_float = 5.5
print(my_integer + my_float)  # Output: 15.5

big_number = 10 ** 1000
print(big_number)  # Output: very big number

my_int = 1
my_float = float(my_int)
print(my_float)  # Output: 1.0

my_float = 1.9999
my_int = int(my_float)
print(my_int)  # Output: 1

my_float = 1.9999
my_int = round(my_float)
print(my_int)  # Output: 2


# задание
# В высотном доме 5 подъездов по 20 квартир каждый. На каждом этаже 4 квартиры. Нумерация квартир идёт подряд, снизу
# вверх:
# на 1м этаже, 1го подъезда находятся квартиры 1, 2, 3, 4.
# на 2м этаже, 1го подъезда находятся квартиры 5, 6, 7, 8 и т.д.
# Напишите скрипт, который получает номер квартиры и выводит на экран номер подъезда и этажа.
# Протестируйте скрипт на разных значениях входных данных.

#  решение
flat_number = 9
entrance_number = 1 + (flat_number - 1) // 20
floor_number = 1 + (flat_number - 1) % 20 // 4

print("Entrance_number: ", entrance_number, "Floor number: ", floor_number)


is_student = True
is_graduated = False
print(is_student, is_graduated)  # Outputs: True False

x = 10
y = 10
print(x == y)  # Outputs: True

x = 9
y = 10
print(x == y)  # Outputs: False

x = 10
y = 10
is_equal = x == y
print(is_equal)  # Outputs: True
print(x != y)  # Outputs: False
print(x >= y)  # Outputs: True

x = 10
y = 9
print(x > y)  # Outputs: True
print(x < y)  # Outputs: False
print(x >= y)  # Outputs: True
print(x <= y)  # Outputs: False

x = 10
y = 10
print(x >= y)  # Outputs: True
print(x <= y)  # Outputs: True

x = 1
print(x < 5 and x > -2)  # Outputs: True

x = 6
print(x < 5 and x > -2)  # Outputs: False

is_student = True
print(not is_student)  # Outputs: False

print(bool(1))  # Outputs: True
print(bool(0))  # Outputs: False
print(bool(-1))  # Outputs: True

print(bool("Hello, world"))  # Outputs: True
print(bool(""))  # Outputs: False

print(int(True))  # Outputs: 1
print(int(False))  # Outputs: 0



"""Задание 1
Выведите на экран надпись Nothing will work unless
you do на разных строках. Пример вывода:
Nothing
will work
unless you do.

Задание 2
Выведите на экран надпись "Anyonewho stopslearning
is old, whether at twenty or eighty" Henry Ford на разных
строках. Пример вывода:
“Anyone who
 stops
 learning is old,
 whether at twenty or eighty”.
 Henry Ford
 
Задание 3
Пользователь вводит с клавиатуры два числа. Необходимо найти сумму чисел, разницу чисел, произведение
числе. Результат вычислений вывести на экран.
1

Задание 4
Пользователь вводит с клавиатуры два числа. Первое
число — это значение, второе число процент, который
необходимо посчитать. Например, мы ввели с клавиатуры
50 и 10. Требуется вывести на экран 10 процентов от 50.
Результат: 5

Задание 5
Напишите программу, вычисляющую площадь прямоугольника. Пользователь с клавиатуры вводит ширину
и высоту прямоугольника."""


"""Реализуйте программу, которая будет вычислять количество различных объектов в списке.
Два объекта a и b считаются различными, если a is b равно False.

Вашей программе доступна переменная с названием objects, которая ссылается на список, содержащий не более 100 объектов. 
Выведите количество различных объектов в этом списке."""

objects = [1, 2, 1, 2, 3]
ans = 0
objects2 = []
for obj in objects: # доступная переменная objects
    if obj not in objects2:
        objects2.append(obj)

print(len(objects2))

# Больше задач на: https://education.yandex.ru/handbook/python