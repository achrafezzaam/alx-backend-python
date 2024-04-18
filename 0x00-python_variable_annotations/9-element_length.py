#!/usr/bin/env python3
''' Define the element_length function '''
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    ''' Return a list of tuples containing the index and length
        of each element of lst '''
    return [(i, len(i)) for i in lst]
