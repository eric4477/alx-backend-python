#!/usr/bin/env python3
"""
Module that provides a function to get the length
of each element in a list.
"""

from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Takes a list of strings and returns a list of tuples.
    """
    return [(i, len(i)) for i in lst]
