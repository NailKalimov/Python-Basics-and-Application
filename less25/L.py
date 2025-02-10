# Принцип замещения Лисков (Liskov Substitution Principle, LSP)
from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def set_properties(self, color, gear, capacity):
        pass

    @abstractmethod
    def get_properties(self):
        pass


class Sedan(Car):
    def __init__(self):
        self.type = "sedan"
        self.color = None
        self.gear = None
        self.capacity = None

    def set_properties(self, color, gear, capacity):
        self.color = color
        self.gear = gear
        self.capacity = capacity

    def get_properties(self):
        return self.color, self.gear, self.capacity


class Coupe(Car):
    def __init__(self):
        self.type = "coupe"
        self.color = None
        self.gear = None
        self.capacity = None
        self.max_speed = None

    def set_properties(self, color, gear, capacity, max_speed=None):
        self.color = color
        self.gear = gear
        self.capacity = capacity
        self.max_speed = max_speed

    def get_properties(self):
        return self.color, self.gear, self.capacity, self.max_speed


def find_red_cars(lst: list[Car]):
    res = 0
    for car in lst:
        res += 1 if car.get_properties()[0] == "red" else 0
    return res


polo = Sedan()
polo.set_properties('red', 5, 5)
fiesta = Coupe()
fiesta.set_properties('blue', 5, 4)

print(find_red_cars([fiesta, polo]))
"""
Функция find_red_cars работает с подклассом класса Car не зная об этом - Прицип замещения Лисков выполняется
"""