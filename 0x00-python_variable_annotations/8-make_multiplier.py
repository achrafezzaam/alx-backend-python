#!/usr/bin/env python3
''' Define the make_multiplier function '''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable([float], float):
    ''' Returns a function that multiplies a float by multiplier '''
    return lambda x: x * multiplier
