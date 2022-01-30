import asyncio
#
# def foo():
#     return 2
#
#
#
# foo()
# print("tim")

#this is sync foo is run b4 sync


#async
# async def main():
#     print('tim')
#     task = asyncio.create_task(foo('text')) #create a task
#     await task #waits for the task to finish b4 u move to  nxt line
#     print('finished')
#
#
# async def foo(text):
#     print(text)
#     await asyncio.sleep(1)
#
#
# #any time u use async.sleep it pauses execution and runs another
# so if fun 1 sleep 0.25 and fun 2 is 1 it it runs 4 tyms the moves to func 2 based on tym
# #run async func
# asyncio.run(main())


async def fetch_data():
    print('start fetching')
    await asyncio.sleep(2)
    print('done fetching')
    return {'data': 1}


async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)


async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())

    value = await task1
    print(value)
    await task2



asyncio.run(main())
import asyncio
#
# def foo():
#     return 2
#
#
#
# foo()
# print("tim")

#this is sync foo is run b4 sync


#async
# async def main():
#     print('tim')
#     task = asyncio.create_task(foo('text')) #create a task
#     await task #waits for the task to finish b4 u move to  nxt line
#     print('finished')
#
#
# async def foo(text):
#     print(text)
#     await asyncio.sleep(1)
#
#
# #any time u use async.sleep it pauses execution and runs another
# so if fun 1 sleep 0.25 and fun 2 is 1 it it runs 4 tyms the moves to func 2 based on tym
# #run async func
# asyncio.run(main())


async def fetch_data():
    print('start fetching')
    await asyncio.sleep(2)
    print('done fetching')
    return {'data': 1}


async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)


async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())

    value = await task1
    print(value)
    await task2



asyncio.run(main())