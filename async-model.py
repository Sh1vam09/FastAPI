import asyncio
import time
from timeit import default_timer as timer


async def run_task(
    name, seconds
):  # you need to define where you want async and where the it get delay over tehre you need t define await
    print(f"{name} started at: {timer()}")
    await asyncio.sleep(seconds)
    print(f"{name} completed at: {timer()}")


# the async functions should be called in the async loop only
# you use gather it act as a loop that tells that these function to perform in async
async def main():
    start = timer()
    await asyncio.gather(
        run_task("Task 1", 2), run_task("Task 2", 1), run_task("Task 3", 3)
    )
    print(f"\nTotal time taken: {timer() - start:.2f} s")


asyncio.run(main())
