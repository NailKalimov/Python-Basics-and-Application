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
