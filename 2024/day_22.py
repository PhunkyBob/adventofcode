"""
Advent of Code 2024
--- Day 22: Monkey Market ---
https://adventofcode.com/2024/day/22

"""

from typing import Any, Callable, Dict, List

from aoc_performance import aoc_perf
from aoc_utils import download_input

DAY = "22"


def read_input(input_filename: str) -> List[int]:
    with open(input_filename, "r") as file:
        return list(map(int, file.read().splitlines()))


from typing import Generator


def evolve_secret(secret: int) -> Generator[int, None, None]:
    while True:
        secret = mix(secret, secret * 64)
        secret = prune(secret)
        secret = mix(secret, secret // 32)
        secret = prune(secret)
        secret = mix(secret, secret * 2048)
        secret = prune(secret)
        yield secret


def mix(secret: int, value: int) -> int:
    return value ^ secret


def prune(secret: int) -> int:
    return secret % 16777216


def part_A(input_filename: str) -> int:
    initial_secrets = read_input(input_filename)
    result = 0
    for secret in initial_secrets:
        generator = evolve_secret(secret)
        for _ in range(2000):
            value = next(generator)
        result += value
    return result


def part_B(input_filename: str) -> int:
    return 0


def main() -> None:
    download_input(DAY, 2024)
    input_filename = f"day_{DAY}_input_sample.txt"
    input_filename = f"day_{DAY}_input.txt"

    with aoc_perf(memory=False):
        print(f"Day {DAY} Part A")
        answer = part_A(input_filename)
        print(f"Answer: {answer}")

    with aoc_perf(memory=False):
        print(f"Day {DAY} Part B")
        answer = part_B(input_filename)
        print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
