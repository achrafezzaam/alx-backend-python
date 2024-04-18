#!/usr/bin/env python3
''' Define the sum_mixed_list function '''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    ''' Return the sum of a list content '''
    return float(sum(mxd_lst))
