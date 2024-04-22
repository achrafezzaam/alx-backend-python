#!/usr/bin/env python3
''' Define the task_wait_n function '''
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    ''' Run wait_random n times '''
    times = await asyncio.gather(
            *tuple(map(lambda x: task_wait_random(max_delay), range(n)))
            )
    return sorted(times)
