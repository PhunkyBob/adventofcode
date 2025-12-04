"""
Advent of Code 2023
--- Day 15: Lens Library ---
https://adventofcode.com/2023/day/15


- Determine the ASCII code for the current character of the string.
- Increase the current value by the ASCII code you just determined.
- Set the current value to itself multiplied by 17.
- Set the current value to the remainder of dividing itself by 256.
"""

from typing import Any, Callable, Dict, List

from aoc_performance import aoc_perf
from aoc_utils import download_input

DAY = "15"


def read_input(input_filename: str) -> str:
    with open(input_filename, "r") as f:
        return f.read().strip()


def aoc_hash(data: str) -> int:
    current_value = 0
    for char in data:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value


def get_focusing_power(boxes: List[Dict[str, int]]) -> int:
    return sum(
        (box_no + 1) * (slot + 1) * box[key] for box_no, box in enumerate(boxes) for slot, key in enumerate(box.keys())
    )


def part_A(input_filename: str) -> int:
    data = read_input(input_filename)
    return sum(aoc_hash(element) for element in data.split(","))


def part_B(input_filename: str) -> int:
    data = read_input(input_filename)
    boxes: List[Dict[str, int]] = [{} for _ in range(256)]
    for element in data.split(","):
        if "=" in element:
            key, value = element.split("=")
            hash_key = aoc_hash(key)
            boxes[hash_key][key] = int(value)
        elif "-" in element:
            key = element.split("-")[0]
            hash_key = aoc_hash(key)
            if key in boxes[hash_key]:
                del boxes[hash_key][key]

    return get_focusing_power(boxes)


def main() -> None:
    download_input(DAY, 2023)
    input_filename = f"day_{DAY}_input.txt"
    # input_filename = f"day_{DAY}_input_sample.txt"

    with aoc_perf(memory=False):
        print(f"Day {DAY} Part A")
        answer = part_A(input_filename)
        print(f"Answer: {answer}")
        # Expected answer: 517315

    with aoc_perf(memory=False):
        print(f"Day {DAY} Part B")
        answer = part_B(input_filename)
        print(f"Answer: {answer}")
        # Expected answer: 247763


if __name__ == "__main__":
    main()
