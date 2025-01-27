# https://github.com/pyneng/all-pyneng-slides/blob/main/pyneng/17_serialization.md
"""
Модуль json обеспечивает работу со стандартными файлами JSON. Это широко используемый формат обмена
данными, удобный для чтения и не зависящий от языка программирования. С помощью модуля json вы можете
сериализовать и десериализовать стандартные типы данных Python:
    bool
    dict
    int
    float
    list
    string
    tuple
    None
"""
import json

data = {"Russia": "Moscow", "Germany": "Berlin", "France": "Paris", "USA": "Washington", "South Korea": "Seul"}

with open('file.json', 'w') as f:
    json.dump(data, f, sort_keys=True)

with open('file.json', 'r') as f:
    input_data = json.load(f)

print(input_data)

############## Сериализация встроенных типов данных Python с помощью модуля pickle
import pickle

'''Возвращает измененное представление объекта obj в виде объекта bytes, вместо записи его в файл.'''
data = [1, 2, 3, "a", "b", "c"]
pickled_string = pickle.dumps(data)
print(pickled_string)

'''Возвращает восстановленную иерархию объектов данных расширенного представления объекта. 
данные должны быть объектом bytes-like object.'''
print(pickle.loads(pickled_string))

########## Сериализация класса с помощью модуля pickle
'''Модуль pickle специфичен для Python — результаты сериализации могут быть прочитаны только другой программой на Python.
Модуль pickle сериализует гораздо больше типов, чем json. Но всё-таки не все.
'''


class example_class:
    a_number = 35
    a_string = "hey"
    a_list = [1, 2, 3]
    a_dict = {"first": "a", "second": 2, "third": [1, 2, 3]}
    a_tuple = (22, 23)


my_object = example_class()
with open('custom_object_repr.txt', "w") as f:
    f.write(repr(my_object))
my_pickled_object = pickle.dumps(my_object)  # Pickling the object
print(f"\nThis is my pickled object:\n{my_pickled_object}\n")

my_unpickled_object = pickle.loads(my_pickled_object)  # Unpickling the object
print(f"This is a_dict of the unpickled object:\n{my_unpickled_object.a_dict}\n")

# Сериализация класса с помощью json
# https://code.tutsplus.com/ru/serialization-and-deserialization-of-python-objects-part-1--cms-26183t
from datetime import datetime


class A(object):
    def __init__(self, simple=None):
        self.simple = simple

    def __eq__(self, other):
        if not hasattr(other, 'simple'):
            return False
        return self.simple == other.simple

    def __ne__(self, other):
        if not hasattr(other, 'simple'):
            return True
        return self.simple != other.simple


simple = dict(int_list=[1, 2, 3],
              text='string',
              number=3.44,
              boolean=True,
              none=None)
complex_obj = dict(a=A(simple), when=datetime(2016, 3, 7))
print("Complex object : ", complex_obj)
"""JSON имеет очень ограниченную систему типов и не может автоматически сериализовать пользовательские классы. 
Способ обращения к ней заключается в подклассе класса JSONEncoder, используемого модулем json, и реализации default(), 
которая вызывается всякий раз, когда кодер JSON запускается в объект, который он не может сериализовать.
"""


# Кастомный сериализатор
class CustomEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return {'__datetime__': o.replace(microsecond=0).isoformat()}
        return {'__{}__'.format(o.__class__.__name__): o.__dict__}
        # return {f'__{o.__class__.__name__}__': o.__dict__}


serialized = json.dumps(complex_obj, indent=4, cls=CustomEncoder)
print(serialized)


# Кастомный сериализатор можно так же определить в виде функции(см. Doc json.dumps(...default=func)) или в виде метода объекта
class MyClass:
    def __init__(self, x):
        self.x = x


def class_to_dict(obj):
    return obj.__dict__


import json

obj = MyClass(5)
json.dumps(obj, default=class_to_dict)


# Custom Deserializer
def decode_object(o):
    if '__A__' in o:
        a = A()
        a.__dict__.update(o['__A__'])
        return a
    elif '__datetime__' in o:
        return datetime.strptime(o['__datetime__'], '%Y-%m-%dT%H:%M:%S')
    return o


deserialized = json.loads(serialized, object_hook=decode_object)
print(deserialized)
print(deserialized == complex_obj)
