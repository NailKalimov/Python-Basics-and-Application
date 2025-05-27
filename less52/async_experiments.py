import time
import asyncio

async def coro_1():
    print("корутина 1. Выполняюсь")
    await asyncio.sleep(2)
    print("корутина 1. Готово!")


async def coro_2():
    print("корутина 2. Выполняюсь")
    await asyncio.sleep(2)
    print("корутина 2. Готово!")

async def main():
    # await asyncio.create_task(coro_1())
    # await asyncio.create_task(coro_2())

    # asyncio.create_task(coro_1())
    # await asyncio.create_task(coro_2())

    await asyncio.gather(coro_1(), coro_2())

print(time.strftime('%S'))
asyncio.run(main())
print(time.strftime('%S'))
    

"""
Пример плохого асинхронного кода
"""
# async def coro_1():
#     print("корутина 1. Выполняюсь")
#     await asyncio.sleep(2)


# async def coro_5():
#     print("Вызываю корутину 3")
#     await coro_3()
#     await asyncio.sleep(2)



# async def coro_3():
#     print("Вызываю корутину 2")
#     await coro_2()
#     await asyncio.sleep(2)



# async def coro_4():
#     print("Вызываю корутину 1")
#     await coro_1()
#     await asyncio.sleep(2)



# async def coro_2():
#     print("Вызываю корутину 4")
#     await coro_4()
#     await asyncio.sleep(2)



# print(time.strftime('%S'))
# asyncio.run(coro_5())
# print(time.strftime('%S'))
