# Создание нового класса вызовом конструктора мета-класса
print(type('A', (object,), {}))
print(type('A', (object,), {}).__bases__)
print(type('A', (object,), {}).__class__)


# ~ Классическое создание класса из мета-класса type
class B(object):  # ~ type(classname, superclasses, attributes_dict)
    x = 1


print(B)
print(B.__bases__)
print(B.__class__)

print('')
# Создание нового мета-класса и создание нового класса на его основе
class Meta(type):
    def __new__(mcls, name, bases, attrs):
        print('creating new class', name)
        return super(Meta, mcls).__new__(mcls, name, bases, attrs)

    def __init__(cls, name, bases, attrs):
        print('initing new class', name)

C = Meta('C', (object,), {'x': 1})
print(C.__dict__)
print(C.__bases__)
print(C.__class__)


# ~
class D(object, metaclass=Meta):
    x = 1


print(D)
print(D.__bases__)
print(D.__class__)
