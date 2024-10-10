#!/usr/bin/env python3
"""Define the sum_list function with type annotations"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of a list of floats.

    Args:
        input_list (List[float]): A list of floats to sum.

    Returns:
        float: The sum of the list elements.
    """
    return sum(input_list)
