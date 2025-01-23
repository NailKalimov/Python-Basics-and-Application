from less3 import objects

lst = [123, 123]
if isinstance(lst, object):
    print("lst is a subclass of object")

if type(lst) == list:
    print("It is list!")
elif type(lst) == object:
    print("it is object!")
#########################

print(dir(object()))
print(sorted(object().__dir__()))


################ setattr и delattr влияют только на атрибуты объекта
class B(object):
    qux = 'B'
    a=2
    def __init__(self):
        self.name = 'B object'

    def bar(self):
        print('bar')

b = B()
b.a = 1 # ~setattr(x, 'y', v) is equivalent to ``x.y = v``
print(f'b.a = {b.a}')
print(f"B.a = {B.a}")
delattr(b,'a')
print(f'b.a = {b.a}')
print(f"B.a = {B.a}")

#########################

print(B.__dict__.keys())
print(B.__dict__.values())
print(B.__class__)# ~ print(type(B))
print(B.__bases__) #parents

###########################