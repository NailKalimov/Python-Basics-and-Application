from aiohttp import ClientSession
import asyncio
from enviroment import apid


async def func(city):
    async with ClientSession() as session:
        url = f'http://api.openweathermap.org/data/2.5/weather'
        params = {'q': city, 'APPID': apid, 'units': 'metric'}
        async with session.get(url, params=params) as resp:
            weather = await resp.json()

        print(f'{city}: {weather['main']}')


async def main(cities_):
    tasks = []
    for city in cities_:
        tasks.append(asyncio.create_task(func(city)))

    for task in tasks:
        await task


cities = ['Izhevsk', 'Moscow', 'Kazan', 'Vladivostok', 'Madrid', 'Ussuriysk', 'Пхеньян', "Ханой"]

asyncio.run(main(cities))