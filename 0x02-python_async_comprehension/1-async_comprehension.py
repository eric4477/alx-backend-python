#!/usr/bin/env python3
"""
This module defines a coroutine that collects random numbers using an
asynchronous comprehension.
"""

from typing import List
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers from async_generator.
    """
    return [num async for num in async_generator()]
