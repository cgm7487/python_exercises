import asyncio

async def foo():
    print('Running in foo')
    await asyncio.sleep(0)
    print('Context switch to foo again')

async def bar():
    print('Context switch to bar')
    await asyncio.sleep(0)
    print('context switch back to bar')

async def main():
    tasks = [foo(), bar()]
    await asyncio.gather(*tasks)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
