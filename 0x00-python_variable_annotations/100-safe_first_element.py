#!/usr/bin/env python3
''' Define the safe_first_element function '''
from typing import Sequence, Optional, Any


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    ''' I have absolutely no idea what this is for '''
    if lst:
        return lst[0]
    else:
        return None
