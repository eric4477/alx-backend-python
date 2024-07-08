#!/usr/bin/env python3
""" Module for creating an asyncio task for wait_random using
    task_wait_random """

from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Waits for random delay using task_wait_random until max_delay,
    returns list of actual delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
