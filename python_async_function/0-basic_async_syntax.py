#!/usr/bin/env python3
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    random_val = random.uniform(0, max_delay)
    await asyncio.sleep(random_val)
    return random_val
