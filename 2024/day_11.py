"""
Advent of Code 2024
--- Day 11: Plutonian Pebbles ---
https://adventofcode.com/2024/day/11

The strange part is that every time you blink, the stones change.
"""

from dataclasses import dataclass
from typing import Dict, List

from aoc_performance import aoc_perf
from aoc_utils import download_input

DAY = "11"


@dataclass
class Stone:
    value: int | List["Stone"]

    def transform(self) -> None:
        if isinstance(self.value, int):
            if self.value == 0:
                self.value = 1
            elif len(str(self.value)) % 2 == 0:
                left_half = str(self.value)[: len(str(self.value)) // 2]
                right_half = str(self.value)[len(str(self.value)) // 2 :]
                self.value = [Stone(int(left_half)), Stone(int(right_half))]
            else:
                self.value *= 2024
        else:
            # Already a list of stones
            for stone in self.value:
                stone.transform()

    def count(self) -> int:
        if isinstance(self.value, int):
            return 1
        else:
            return sum(stone.count() for stone in self.value)


def read_input_as_stones(input_filename: str) -> List[Stone]:
    with open(input_filename, "r") as file:
        return [Stone(int(elem)) for elem in file.read().split(" ")]


def part_A(input_filename: str) -> int:
    stones = read_input_as_stones(input_filename)
    for _ in range(25):
        for stone in stones:
            stone.transform()
    return sum(stone.count() for stone in stones)


def read_input_as_ints(input_filename: str) -> Dict[int, int]:
    with open(input_filename, "r") as file:
        return {int(elem): 1 for elem in file.read().split(" ")}


def transform(stones: Dict[int, int]) -> Dict[int, int]:
    new_stones: Dict[int, int] = {}
    for stone in stones:
        if stone == 0:
            new_stones[1] = new_stones.get(1, 0) + stones[stone]
        elif len(str(stone)) % 2 == 0:
            left_half = str(stone)[: len(str(stone)) // 2]
            right_half = str(stone)[len(str(stone)) // 2 :]
            new_stones[int(left_half)] = new_stones.get(int(left_half), 0) + stones[stone]
            new_stones[int(right_half)] = new_stones.get(int(right_half), 0) + stones[stone]
        else:
            new_stones[stone * 2024] = new_stones.get(stone * 2024, 0) + stones[stone]
    return new_stones


def part_B(input_filename: str) -> int:
    stones = read_input_as_ints(input_filename)
    for _ in range(75):
        stones = transform(stones)
    return sum(stones.values())


def main() -> None:
    download_input(DAY, 2024)
    # input_filename = f"day_{DAY}_input_sample.txt"
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
