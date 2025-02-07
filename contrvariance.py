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
from collections.abc import Callable


def give_tasks_for_programmer(
        task: Callable[[Programmer], None],
        prog: Programmer) -> None:
    task(prog)


def task_for_programmer(p: Programmer) -> None:
    p.fix_bug_in_code(1)


def task_for_employee(e: Employee) -> None:
    e.pay_salary(10000)


def task_for_frontender(f: Frontender) -> None:
    f.realize_markup()


give_tasks_for_programmer(task_for_programmer, programmer)
give_tasks_for_programmer(task_for_employee, programmer)
# Аргументы функции являются контрвариативными, т.е. можно передать ф-ю, которая в качестве аргументов принимает более старшие классы
# см 42 стр
give_tasks_for_programmer(task_for_frontender, frontender)
