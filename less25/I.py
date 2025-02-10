# Принцип разделения интерфейсов (Interface Segregation Principle, ISP)
from abc import ABC, abstractmethod


class Walkable(ABC):
    @abstractmethod
    def walk(self):
        pass


class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass


class Ostrich(Walkable):
    def walk(self):
        print("Ostrich is walking")


class Eagle(Walkable, Flyable):
    def fly(self):
        print("Eagle is flying")

    def walk(self):
        print("Eagle is walking")


try:
    obj = Eagle()
    obj.fly()
    obj.walk()
    obj2 = Ostrich()
    obj2.walk()

except Exception as e:
    print(e)
"""
вместо одного большого общего интерфейса сделали два легковесных и в подклассах теперь есть только те меды, которые 
имеют полноценную реализацию и будут использоваться в дальнейшем  
"""