import asyncio
from aiohttp import ClientSession

async def test_async_post(stockId):

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    async with ClientSession() as session:
        async with session.post("http://localhost:5000/price", headers = headers, data="stock_id="+stockId) as resp:
            print(await resp.text())


async def main():
    tasks = [test_async_post("2412"), test_async_post("0050"), test_async_post("1234")]
    await asyncio.gather(*tasks)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close


