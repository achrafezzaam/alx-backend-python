#!/usr/bin/env python3
''' Define the to_kv function '''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    ''' Build a tuple from a given string and the square of a number '''
    return (k, float(v**2))
