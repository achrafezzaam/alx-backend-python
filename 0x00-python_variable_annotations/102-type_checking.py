#!/usr/bin/env python3
''' Define the zoom_array function and a few variables '''
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    ''' Please document your code '''
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: Tuple = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
