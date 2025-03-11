# jarvis/utils/async_tools.py
# Async utilities
import asyncio

async def run_async_task(task):
    await asyncio.create_task(task)
