#!/usr/bin/env python3
"""Define the make_multiplier function with type annotations"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies its input by the given multiplier.

    Args:
        multiplier (float): The multiplier to use.

    Returns:
        Callable[[float], float]: A function that takes a float and
        returns a float.
    """
    def multiplier_function(value: float) -> float:
        """Multiplies the input value by the multiplier."""
        return value * multiplier

    return multiplier_function
