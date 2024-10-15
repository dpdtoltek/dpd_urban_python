import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    ball = 1
    for i in range(5):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {ball} шар.')
        ball += 1
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Maxim', 4))
    task2 = asyncio.create_task(start_strongman('Oleg', 3))
    task3 = asyncio.create_task(start_strongman('Ivan', 5))
    await task1
    await task2
    await task3


asyncio.run(start_tournament())
