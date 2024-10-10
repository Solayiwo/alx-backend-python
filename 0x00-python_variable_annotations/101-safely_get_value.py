#!/usr/bin/env python3
"""Adding type annotations to safely_get_value function"""

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely get the value from the dictionary for the given key.
    If the key doesn't exist, return the default value.

    Parameters:
    dct (Mapping): The dictionary to retrieve the value from.
    key (Any): The key to search in the dictionary.
    default (Union[T, None]): The default value to return if the key is
    not found.

    Returns:
    Union[Any, T]: The value from the dictionary if the key is found,
    otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
