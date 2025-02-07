class Car:
    def __init__(self, t):
        self.type = t


class PetrolCar(Car):
    pass


car = Car("Suv")
car.properties = {'color': 'red', 'gear': 5, 'capacity': 1}
petrol_car = PetrolCar('sedan')
petrol_car.properties = ("blue", 3, 5)
cars = [car, petrol_car]
res = 0
for car in cars:
    if car.properties['color'] == 'red':
        res += 1
print(f"Number of red cars = {res}")
'''Мы пытаемся просмотреть список объектов Car. Именно здесь мы нарушаем принцип подстановки Лисков, поскольку мы не можем 
заменить объекты супертипа Car объектами подтипа PetrolCar внутри функции поиска красных автомобилей.'''
###############################################

# from abc import ABC, abstractmethod
#
#
# class Car(ABC):
#     @abstractmethod
#     def set_properties(self, color, gear, capacity):
#         pass
#
#     @abstractmethod
#     def get_properties(self):
#         pass
#
#
# class Sedan(Car):
#     def __init__(self):
#         self.type = "sedan"
#         self.color = None
#         self.gear = None
#         self.capacity = None
#
#     def set_properties(self, color, gear, capacity):
#         self.color = color
#         self.gear = gear
#         self.capacity = capacity
#
#     def get_properties(self):
#         return self.color, self.gear, self.capacity
#
#
# class Coupe(Car):
#     def __init__(self):
#         self.type = "coupe"
#         self.color = None
#         self.gear = None
#         self.capacity = None
#         self.max_speed = None
#
#     def set_properties(self, color, gear, capacity, max_speed=None):
#         self.color = color
#         self.gear = gear
#         self.capacity = capacity
#         self.max_speed = max_speed
#
#     def get_properties(self):
#         return self.color, self.gear, self.capacity, self.max_speed
#
#
# def find_red_cars(lst: list[Car]):
#     res = 0
#     for car in lst:
#         res += 1 if car.get_properties()[0] == "red" else 0
#     return res
#
#
# polo = Sedan()
# polo.set_properties('red', 5, 5)
# fiesta = Coupe()
# fiesta.set_properties('blue', 5, 4)
#
# print(find_red_cars([fiesta, polo]))
