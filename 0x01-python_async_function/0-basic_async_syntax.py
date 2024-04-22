#!/usr/bin/env python3
''' Define the wait_random function '''
import asyncio
from random import random


async def wait_random(max_delay: int = 10) -> float:
    ''' Wait for a random time '''
    w_time = random() * max_delay
    await asyncio.sleep(w_time)
    return w_time
