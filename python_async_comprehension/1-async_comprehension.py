#!/usr/bin/env python3
import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    '''coroutine will loop 10 times, each time asynchronously wait 1 second'''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


async def async_comprehension() -> typing.Generator[float, None, None]:
    '''then return the 10 random numbers.'''
    return [num async for num in async_generator()][:10]
