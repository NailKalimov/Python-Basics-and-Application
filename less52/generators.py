


'''
yeld from
'''
def gen_function(n):
    while n > 0:
        try:
            value = yield n
            print("Got value: ", value)
        except ValueError as e:
            print("Got exception: ", e)

        n -= 1

    return value

gen = gen_function(3)
gen_2 = gen_function(5)


def main():
    yield from gen
    yield from gen_2

main_gen = main()

print(next(main_gen))
print(main_gen.send(55))
print(main_gen.throw(ValueError("oops")))

print(next(main_gen))
print(main_gen.send(77))
print(main_gen.throw(ValueError("oops")))