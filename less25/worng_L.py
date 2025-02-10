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
