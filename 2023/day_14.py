"""
Advent of Code 2023
--- Day 14: Parabolic Reflector Dish ---
https://adventofcode.com/2023/day/14

"""
from typing import List, Dict
from aoc_performance import aoc_perf


DAY = "14"


def read_input(input_filename: str) -> List[str]:
    """WARNING: North will be the right side of the matrix."""
    with open(input_filename, "r") as f:
        return ["".join(line) for line in zip(*f.readlines()[::-1])]


def display(lines: List[str]) -> None:
    for line in ["".join(comb) for comb in zip(*[line[::-1] for line in lines])]:
        print(line)
    print()


def get_total_load(lines: List[str]) -> int:
    return sum(col + 1 for line in lines for col, char in enumerate(line) if char == "O")


def rotate(lines: List[str]) -> List[str]:
    """Rotate a matrix 90 degrees clockwise."""
    return ["".join(line) for line in zip(*lines[::-1])]


def tilt(lines: List[str]) -> List[str]:
    """Split the lines by "#", remove the "O" from the left side of the chunks and add them to the right side."""
    return ["#".join([chunk.replace("O", "") + "O" * chunk.count("O") for chunk in line.split("#")]) for line in lines]


def part_A(input_filename: str) -> int:
    lines = read_input(input_filename)
    new_lines = tilt(lines)
    # display(new_lines)
    return get_total_load(new_lines)


def part_B(input_filename: str) -> int:
    lines = read_input(input_filename)
    steps = 1000000000
    i = 0
    memory: Dict[int, int] = {}
    while i < steps:
        key = hash(tuple(lines))
        if key in memory:
            print(f"Found a match: step {i} == step {memory[key]}")
            loop_size = i - memory[key]
            remains = (steps - i) % loop_size
            i = steps - remains
        for _ in range(4):
            lines = tilt(lines)
            lines = rotate(lines)
        memory[key] = i
        if i % 1000 == 0:
            print(f"Step {i}")
        i += 1
    # display(lines)
    return get_total_load(lines)


def main() -> None:
    input_filename = f"day_{DAY}_input.txt"
    # input_filename = f"day_{DAY}_input_sample.txt"

    with aoc_perf(memory=False):
        print(f"Day {DAY} Part A")
        answer = part_A(input_filename)
        print(f"Answer: {answer}")
        # Expected: 113078

    with aoc_perf(memory=False):
        print(f"Day {DAY} Part B")
        answer = part_B(input_filename)
        print(f"Answer: {answer}")
        # Expected: 94255


if __name__ == "__main__":
    main()
