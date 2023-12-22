"""
Advent of Code 2023
--- Day 8: Haunted Wasteland ---
https://adventofcode.com/2023/day/8

"""
from typing import Any, Callable, List, Dict, Tuple
from aoc_performance import aoc_perf
import re
from math import lcm

DAY = "08"


def lcm_of_list(numbers):
    result = 1
    for num in numbers:
        result = lcm(result, num)
    return result


def read_input(input_filename: str) -> Tuple[str, Dict[str, Dict[str, str]]]:
    data: Dict[str, Dict[str, str]] = {}
    with open(input_filename, "r") as input_file:
        lines = input_file.read().splitlines()
        directions = lines[0]
        for line in lines[2:]:
            if res := re.match(r"(.+) = \((.+), (.+)\)", line):
                key, left, right = res.groups()
                data[key] = {"L": left, "R": right}
    return directions, data


def part_A(input_filename: str) -> int:
    directions, data = read_input(input_filename)
    current = "AAA"
    steps = 0
    while current != "ZZZ":
        current = data[current][directions[steps % len(directions)]]
        steps += 1
    return steps


def part_B(input_filename: str) -> int:
    directions, data = read_input(input_filename)

    currents = [d for d in data.keys() if d[-1] == "A"]
    steps_list = []
    for current in currents:
        steps = 0
        while not current.endswith("Z"):
            current = data[current][directions[steps % len(directions)]]
            steps += 1
        steps_list.append(steps)
    return lcm_of_list(steps_list)


def main() -> None:
    input_filename = f"day_{DAY}_input.txt"
    # input_filename = f"day_{DAY}_input_sample.txt"

    with aoc_perf(memory=False):
        print(f"Day {DAY} Part A")
        answer = part_A(input_filename)
        print(f"Answer: {answer}")
        # Expected: 18157

    with aoc_perf(memory=False):
        print(f"Day {DAY} Part B")
        answer = part_B(input_filename)
        print(f"Answer: {answer}")
        # Expected: 14299763833181


if __name__ == "__main__":
    main()
