#!/usr/bin/env python3
''' Define the wait_n function '''
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    ''' Run wait_random n times '''
    times = await asyncio.gather(
            *tuple(map(lambda x: wait_random(max_delay), range(n)))
            )
    return sorted(times)
