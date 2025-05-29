import asyncio


x=0

async def inc():
    global x
    c=x
    c += 1
    await asyncio.sleep(0)
    x = c

async def main():
    await asyncio.gather(*[inc() for _ in range(10)])

asyncio.run(main())
    
print(x)