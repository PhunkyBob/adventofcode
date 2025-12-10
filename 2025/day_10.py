"""
Advent of Code 2025

https://adventofcode.com/2025/day/10

"""

import re
from typing import Any, Callable, Dict, List, Set, Tuple

from aoc_performance import aoc_perf
from aoc_utils import download_input

DAY = "10"

Diagram = int
Button = int
Joltage = List[int]

Machine = Tuple[Diagram, List[Button], Joltage]

Step = Tuple[Diagram, List[Button], Button]


def read_input(input_filename: str) -> List[Machine]:
    machines: List[Machine] = []
    with open(input_filename, "r") as file:
        for line in file.read().splitlines():
            if res := re.findall(r"\[([\.#]+)\] (.+) \{([\d,]+)\}", line):
                diagram_str, buttons_str, joltage_str = res[0]
                diagram = int("".join("1" if c == "#" else "0" for c in diagram_str[::-1]), 2)
                buttons = [sum(2**v for v in map(int, btn[1:-1].split(","))) for btn in buttons_str.split(" ")]
                joltage = list(map(int, joltage_str.split(",")))
                machines.append((diagram, buttons, joltage))
    return machines


def press_button(diagram: Diagram, button: Button) -> Diagram:
    return diagram ^ button


def process_machine(machine: Machine) -> int:
    diagram, buttons, joltage = machine
    values: Dict[int, List[Button]] = {but: [but] for but in buttons}

    length = 1
    while diagram not in values:
        for val in list(values.keys()):
            if len(values[val]) != length:
                continue
            for but in buttons:
                new_val = press_button(val, but)
                if new_val not in values:
                    values[new_val] = values[val] + [but]
        length += 1

    return length


def part_A(input_filename: str) -> int:
    machines = read_input(input_filename)
    return sum(process_machine(machine) for machine in machines)


def part_B(input_filename: str) -> int:
    return 0


def main() -> None:
    download_input(DAY, 2025)
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
