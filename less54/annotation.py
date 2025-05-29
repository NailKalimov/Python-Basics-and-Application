def get_full_name(first_name, last_name):
    full_name = first_name.title() + " " + last_name.title()
    return full_name


print(get_full_name("john", "doe"))

# Type annotation
def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name


print(get_full_name("john", "doe"))

# Type check
def get_name_with_age(name: str, age: int):
    name_with_age = name + " is this old: " + age
    return name_with_age

# Other simple types
def get_items(item_a: str, item_b: int, item_c: float, item_d: bool, item_e: bytes):
    return item_a, item_b, item_c, item_d, item_d, item_e

# Generic types
from typing import List
from typing import Set, Tuple
from typing import Dict


def process_items(items: List[str]):
    for item in items:
        print(item)


def process_items(items_t: Tuple[int, int, str], items_s: Set[bytes]):
    return items_t, items_s


def process_items(prices: Dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)

"""
Вы также можете использовать Optional, чтобы объявить, что переменная 
имеет тип, например, str, но это является «необязательным», 
что означает, что она также может быть None:
"""
from typing import Optional


def say_hi(name: Optional[str] = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")

# Custom types
class Person:
    def __init__(self, name: str):
        self.name = name


def get_person_name(one_person: Person):
    return one_person.name


"""
Pydantic является Python-библиотекой для выполнения валидации данных.

Вы объявляете «форму» данных как классы с атрибутами.

И каждый атрибут имеет тип.

Затем вы создаете экземпляр этого класса с некоторыми значениями, и он 
проверяет значения, преобразует их в соответствующий тип (если все верно) 
и предоставляет вам объект со всеми данными.

И вы получаете полную поддержку редактора для этого итогового объекта.
"""
from datetime import datetime
from typing import List, Union

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: Union[datetime, None] = None
    friends: List[int] = []


external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}
user = User(**external_data)
print(user)
# > User id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=[1, 2, 3]
print(user.id)
# > 123

