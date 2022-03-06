import asyncio


async def main():
    print('A')
    await asyncio.sleep(1)
    print('B')


asyncio.run(main())



