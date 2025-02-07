import os


class Output:
    def __init__(self, data, output_type):
        self.output_type = output_type
        self.data = data

    def display(self):
        if self.output_type == "console":
            print(f"{self.data}")

        elif self.output_type == "file":
            file_dir = os.path.dirname(os.path.abspath(__file__))
            os.chdir(file_dir)
            with open('output.txt', 'w') as f:
                f.write(self.data)
        else:
            raise ValueError("Wrong type of output")


obj = Output("some string", "file")
obj.display()





#########################
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