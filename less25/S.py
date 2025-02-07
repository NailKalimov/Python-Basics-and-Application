class User:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0or age >= 130:
            raise ValueError("Age must be between 0 and 130 ")
        self._age = age

    def display(self):
        print(f"{self.name}{self.last_name}{self.age}")

    def input(self):
        self.name = input("Input name:")
        self.last_name = input("Input last name:")
        self.age = int(input("Input age:"))


obj = User("Bill", "Windows", 34)
obj.display()
obj.input()
obj.display()





####################

class User:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    @property
    def age(self):
        return self._age

    # Setter for age includes validation.
    @age.setter
    def age(self, age):
        if age < 0or age >= 130:
            raise ValueError("Age must be between 0 and 130 ")
        self._age = age

# Console class handles user I/O operations.
class Console:
    # Displays user details.
    @staticmethod
    def display(obj):
        print(f"{obj.name}{obj.last_name}{obj.age}")

    # Reads user input from console and returns a User object.
    @staticmethod
    def input():
        name = input("Input name:")
        last_name = input("Input last name:")
        age = int(input("Input age:"))
        return User(name, last_name, age)

# Create a User, display it, take console input to create a new User,
# then display the new User.
obj = User("Bill", "Windows", 34)
Console.display(obj)
obj = Console.input()
Console.display(obj)