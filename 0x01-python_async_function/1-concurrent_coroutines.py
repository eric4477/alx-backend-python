#!/usr/bin/env python3
""" Takes 2 int args, waits for random delay """

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """ Waits for random delay until max_delay, returns list of
    actual delays """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
