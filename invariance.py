class Employee:
    def __init__(self, name: str):
        self.name = name

    def pay_salary(self, salary: int) -> None:
        print(f"Paid salary {salary} for {self.name}")

    def __repr__(self) -> str:
        return f"{type(self).__name__}('{self.name}')"


class Accountant(Employee):
    def calc_salary_for_employee(self, employee: Employee) -> int:
        print(f"{self} calculated salary for {employee.name}")
        return 1000 * len(employee.name)


class Programmer(Employee):
    def fix_bug_in_code(self, bug: int) -> None:
        print(f"{self} fixed #{bug}")


class Frontender(Programmer):
    def realize_markup(self) -> None:
        print(f"{self} realized markup")


class Backender(Programmer):
    def raelize_api(self) -> None:
        print(f"{self} realized api")


employee = Employee("Alexander")
accountant = Accountant("Bak")
programmer = Programmer("Richard")
frontender = Frontender("Simon")
backender = Backender("Jack")

from collections.abc import Sequence

programmers_list: list[Programmer] = []
frontenders_list: list[Frontender] = []
employees_list: list[Employee] = []
print(f'{programmers_list=}')

programmers_list = employees_list
employees_list.append(accountant)
print(f'{programmers_list=}')

programmers_list = frontenders_list
programmers_list.append(backender)
print(f'{frontenders_list=}')
# со списками адекватно работает использование только тех типов, которые были указаны ~ инвариантность