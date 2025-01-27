class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance


class SingletonClass(Singleton):
    pass


class RegularClass():
    pass

Singleton().x=1
x = SingletonClass()
y = SingletonClass()
print(x == y)  # True
print(f"x.x={x.x}, y.x={y.x}")

x = RegularClass()
y = RegularClass()
print(x == y)  # False
################ Using by meta-classes

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SingletonClass(metaclass=Singleton): #Singletone(classname, superclass, attributes_dict) ~ Singleton().__call__(..)
    pass


class RegularClass():
    pass


x = SingletonClass()
y = SingletonClass()
print(x == y)#True

x = RegularClass()
y = RegularClass()
print(x == y) #False

