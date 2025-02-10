# Принцип открытости/закрытости (Open/Closed Principle, OCP)
from abc import ABC, abstractmethod


class Output(ABC):
    def __init__(self, data):
        self.data = data

    @abstractmethod
    def display(self):
        pass


class ConsoleOutput(Output):
    def display(self):
        print(f"{self.data}")


class FileOutput(Output):
    def display(self):
        with open('output.txt', 'w') as f:
            f.write(self.data)


obj = ConsoleOutput("some string")
obj.display()

obj2 = FileOutput("another string")
obj2.display()
