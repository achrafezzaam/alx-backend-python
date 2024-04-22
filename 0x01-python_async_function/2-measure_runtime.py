#!/usr/bin/env python3
''' Define the measure_time function '''
import asyncio
from time import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    ''' Mesure the total execution time for the wait_n function '''
    strt_time = time()
    asyncio.run(wait_n(n, max_delay))
    return (time() - strt_time) / n
