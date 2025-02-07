'''Паттерн Singleton применяется в программировании, когда требуется гарантировать наличие только одного экземпляра
класса и предоставить глобальную точку доступа к этому экземпляру. Это особенно полезно в следующих случаях:

Управление ресурсами. Когда необходимо контролировать доступ к ограниченным ресурсам, таким как соединения с базой
данных или сетевые соединения. Использование Singleton позволяет гарантировать, что ресурс используется эффективно и
не перегружен одновременными запросами.

Глобальные настройки приложения. Singleton может использоваться для хранения глобальных настроек приложения, таких как
конфигурации, которые должны быть доступны из любой части программы.

Логирование и отладка. В системах логирования Singleton может гарантировать, что все сообщения записываются в один файл
или отправляются на один сервер, упрощая анализ и отладку.

Кэширование данных. Для управления кэшем Singleton обеспечивает централизованное хранение данных, предотвращая
дублирование усилий по их обработке.

Синхронизация доступа. В многопоточных приложениях Singleton помогает синхронизировать доступ к общим ресурсам,
обеспечивая безопасность и избегая конфликтов.

Создание уникальных идентификаторов. В некоторых случаях требуется генерировать уникальные идентификаторы, что также
может быть реализовано через Singleton.

Фабричные методы. Singleton часто используется вместе с фабричными методами для создания объектов, обеспечивая при
этом контроль над количеством создаваемых экземпляров.

Работа с внешними сервисами. При взаимодействии с внешними сервисами Singleton может управлять подключением к этим
сервисам, обеспечивая стабильное и надёжное соединение.'''


class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance


class SingletonClass(Singleton):
    pass


class RegularClass():
    pass


Singleton().x = 1
x = SingletonClass()
y = SingletonClass()
print(x == y)  # True
print(f"x.x={x.x}, y.x={y.x}")

x = RegularClass()
y = RegularClass()
print(x == y)  # False


################ Using by meta-classes

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        print("__call__(...)")
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SingletonClass(
    metaclass=Singleton):  # Singletone(classname, superclass, attributes_dict) ~ Singleton().__call__(..)
    pass


class RegularClass():
    pass


x = SingletonClass()
y = SingletonClass()
print(x == y)  # True

x = RegularClass()
y = RegularClass()
print(x == y)  # False



######################

from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any


"""
Для создания итератора в Python есть два абстрактных класса из встроенного
модуля collections - Iterable, Iterator. Нужно реализовать метод __iter__() в
итерируемом объекте (списке), а метод __next__() в итераторе.
"""


class AlphabeticalOrderIterator(Iterator):
    """
    Конкретные Итераторы реализуют различные алгоритмы обхода. Эти классы
    постоянно хранят текущее положение обхода.
    """

    """
    Атрибут _position хранит текущее положение обхода. У итератора может быть
    множество других полей для хранения состояния итерации, особенно когда он
    должен работать с определённым типом коллекции.
    """
    _position: int = None

    """
    Этот атрибут указывает направление обхода.
    """
    _reverse: bool = False

    def __init__(self, collection: WordsCollection, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self) -> Any:
        """
        Метод __next __() должен вернуть следующий элемент в последовательности.
        При достижении конца коллекции и в последующих вызовах должно вызываться
        исключение StopIteration.
        """
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value


class WordsCollection(Iterable):
    """
    Конкретные Коллекции предоставляют один или несколько методов для получения
    новых экземпляров итератора, совместимых с классом коллекции.
    """

    def __init__(self, collection: list[Any] | None = None) -> None:
        self._collection = collection or []


    def __getitem__(self, index: int) -> Any:
        return self._collection[index]

    def __iter__(self) -> AlphabeticalOrderIterator:
        """
        Метод __iter__() возвращает объект итератора, по умолчанию мы возвращаем
        итератор с сортировкой по возрастанию.
        """
        print("!!!")
        return AlphabeticalOrderIterator(self)

    def get_reverse_iterator(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self, True)

    def add_item(self, item: Any) -> None:
        self._collection.append(item)


if __name__ == "__main__":
    # Клиентский код может знать или не знать о Конкретном Итераторе или классах
    # Коллекций, в зависимости от уровня косвенности, который вы хотите
    # сохранить в своей программе.
    collection = WordsCollection()
    collection.add_item("First")
    collection.add_item("Second")
    collection.add_item("Third")
    collection.add_item("Four")

    print("Straight traversal:")
    # print("\n".join(collection))
    # print("")
    for i in collection:
        print(i)

    print("Reverse traversal:")
    # print("\n".join(collection.get_reverse_iterator()), end="")
    for i in collection.get_reverse_iterator():
        print(i)
    print(collection[1])