#!/usr/bin/env python3
"""Augment safe_first_element function with duck-typed annotations"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of a sequence if it exists,
    otherwise returns None.

    Parameters:
    lst (Sequence[Any]): A sequence (e.g., list, tuple, string)
    containing elements of any type.

    Returns:
    Union[Any, None]: The first element of the sequence if it's not
    empty, or None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
