#!/usr/bin/env python3
import asyncio
import random
import typing
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    '''then return the 10 random numbers.'''
    return [number async for number in async_generator()]
