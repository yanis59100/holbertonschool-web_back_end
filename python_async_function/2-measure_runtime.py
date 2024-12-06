#!/usr/bin/env python3
import asyncio
import random
from time import perf_counter

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    s = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = perf_counter() - s
    return elapsed
