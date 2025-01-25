#Создание нового класса вызовом конструктора мета-класса
print(type('A', (object,), {}))
print(type('A', (object,), {}).__bases__)
print(type('A', (object,), {}).__class__)
#~ Классическое создание класса из мета-класса type
class B(object): # ~ type(classname, superclasses, attributes_dict)
    x=1

print(B)
print(B.__bases__)
print(B.__class__)


# Создание нового мета-класса и создание нового класса на его основе
class Meta(type):
    pass

print(Meta('C', (object,), {'x': 1}))
print(Meta('C', (object,), {'x': 1}).__bases__)
print(Meta('C', (object,), {'x': 1}).__class__)
#~
class D(object, metaclass=Meta):
    x = 1

print(D)
print(D.__bases__)
print(D.__class__)