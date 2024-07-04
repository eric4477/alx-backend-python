#!/usr/bin/env python3
"""
Module that provides a function to get the length
of each element in a list.
"""

from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences and returns a list of tuples.
    """
    return [(i, len(i)) for i in lst]
