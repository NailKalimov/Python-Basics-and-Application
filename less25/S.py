# Принцип единой ответственности (Single Responsibility Principle, сокращенно — SRP)
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
        if age < 0 or age >= 130:
            raise ValueError("Age must be between 0 and 130 ")
        self._age = age


class Console:
    @staticmethod
    def display(obj):
        print(f"{obj.name}{obj.last_name}{obj.age}")

    @staticmethod
    def input():
        name = input("Input name:")
        last_name = input("Input last name:")
        age = int(input("Input age:"))
        return User(name, last_name, age)



obj = User("Bill", "Windows", 34)
Console.display(obj)
obj = Console.input()
Console.display(obj)
