#!/usr/bin/env python3
"""Validating and updating function changes"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Takes a tuple and returns a list where each element is repeated
    'factor' times.

    Parameters:
    lst (Tuple): The input tuple of elements.
    factor (int): The repetition factor (default is 2).

    Returns:
    List: A list where each element from the input is repeated by the factor.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)
