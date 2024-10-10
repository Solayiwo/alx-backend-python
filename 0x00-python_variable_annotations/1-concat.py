#!/usr/bin/env python3
"""Define the concat function with type annotations"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenates two strings.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        str: The concatenated result of str1 and str2.
    """
    return "{}{}".format(str1, str2)
