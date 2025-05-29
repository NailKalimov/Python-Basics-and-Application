def gen():
    x=10
    print(x)
    yield x

async def coro():
    x=10
    print(x)


print(gen())
print(coro())