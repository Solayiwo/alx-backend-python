#!/usr/bin/env python3
"""Define the floor function with type annotations"""

import math


def floor(n: float) -> int:
    """
    Returns the floor of a floating-point number.

    Args:
        n (float): The floating-point number to floor.

    Returns:
        int: The floor of the number.
    """
    return math.floor(n)
