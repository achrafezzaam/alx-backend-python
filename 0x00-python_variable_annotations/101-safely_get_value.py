#!/usr/bin/env python3
''' Define the safely_get_value function '''
from typing import TypeVar, Mapping, Any, Optional, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    ''' I have no idea what this code is doing '''
    if key in dct:
        return dct[key]
    else:
        return default
