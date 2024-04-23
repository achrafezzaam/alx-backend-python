#!/usr/bin/env python3
''' Define the async_generator function '''
import asyncio
from random import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    ''' Loop 10 times to generate a random number between 0 and 10 '''
    for i in range(10):
        await asyncio.sleep(1)
        yield random() * 10
