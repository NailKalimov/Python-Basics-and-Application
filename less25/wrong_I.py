from abc import ABC, abstractmethod


class Bird(ABC):
    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def walk(self):
        pass


class Ostrich(Bird):
    def fly(self):
        # Not an appropriate design,
        # violates Interface Segregation Principle (ISP)
        raise Exception("Ostrich is not flying")

    def walk(self):
        print("Ostrich is walking")


class Eagle(Bird):
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
    obj2.fly()
except Exception as e:
    print(e)
