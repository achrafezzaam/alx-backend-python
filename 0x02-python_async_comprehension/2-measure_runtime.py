#!/usr/bin/env python3
''' Define the measure_runtime function '''
import asyncio
from time import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    ''' Run the async_comprehension coroutine four time then return
        the execution time '''
    strt_time = time()
    await asyncio.gather(
            *(async_comprehension() for x in range(4))
            )
    return time() - strt_time
