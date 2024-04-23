#!/usr/bin/env python3
''' Define the async_comprehension function '''
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    ''' Build a list from the async_generator coroutine '''
    return [x async for x in async_generator()]
