#!/usr/bin/env python3
"""
This module defines an asynchronous generator function.
"""

import asyncio
import random


async def async_generator():
    """
    Coroutine that asynchronously generates random numbers.

    This coroutine will loop 10 times, each time asynchronously waiting
    for 1 second, then yielding a random number between 0 and 10.

    Yields:
        float: A random floating-point number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
