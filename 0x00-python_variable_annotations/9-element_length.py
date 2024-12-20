#!/usr/bin/env python3
"""Annotate the function's parameters and return type"""

from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes a list of sequences and returns a list of tuples.
    Each tuple contains an element from the list and its length.
    """
    return [(i, len(i)) for i in lst]
