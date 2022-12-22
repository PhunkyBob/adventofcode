from functools import wraps
import tracemalloc
from time import perf_counter
from dataclasses import dataclass


@dataclass
class aoc_perf:
    """Measure performance of a block"""

    memory: bool = False
    time: bool = True

    def __enter__(self):
        if self.memory:
            tracemalloc.start()
        if self.time:
            self.start_time = perf_counter()
        return self

    def __exit__(self, type, value, traceback):
        if self.memory:
            current, peak = tracemalloc.get_traced_memory()
            print(f"Memory usage:\t\t {current / 10**6:.6f} MB \n" f"Peak memory usage:\t {peak / 10**6:.6f} MB ")
            tracemalloc.stop()
        if self.time:
            finish_time = perf_counter()
            print(f"Time elapsed in seconds: {finish_time - self.start_time:.6f}")
            print()


def aoc_performance(title: str = "", time: bool = True, memory: bool = False):
    """Measure performance of a function"""

    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            print(f"AdventOfCode {title}")
            if memory:
                tracemalloc.start()
            if time:
                start_time = perf_counter()
            result = func(*args, **kwargs)
            print(f"Answer: {result}")
            if memory:
                current, peak = tracemalloc.get_traced_memory()
                print(f"Memory usage:\t\t {current / 10**6:.6f} MB \n" f"Peak memory usage:\t {peak / 10**6:.6f} MB ")
                tracemalloc.stop()
            if time:
                finish_time = perf_counter()
                print(f"Time elapsed in seconds: {finish_time - start_time:.6f}")
            # print(f"Function: {func.__name__}")
            # print(f"Method: {func.__doc__}")

            print(f'{"-"*40}')

            return result

        return inner

    return decorator
