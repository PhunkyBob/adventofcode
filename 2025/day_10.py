"""
Advent of Code 2025
--- Day 10: Factory ---
https://adventofcode.com/2025/day/10

For example:

[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""

import re
from typing import Dict, List, Set, Tuple

from z3 import Int, Optimize

from aoc_performance import aoc_perf
from aoc_utils import download_input

DAY = "10"

Diagram = int
IntButton = int
Button = List[int]
Joltage = List[int]

IntMachine = Tuple[Diagram, List[IntButton], Joltage]
Machine = Tuple[Diagram, List[Button], Joltage]


PATTERN = re.compile(r"\[([\.#]+)\] (.+) \{([\d,]+)\}")


def read_input(input_filename: str) -> List[IntMachine]:
    machines: List[IntMachine] = []
    with open(input_filename, "r") as file:
        for line in file.read().splitlines():
            if res := PATTERN.findall(line):
                diagram_str, buttons_str, joltage_str = res[0]
                diagram = int("".join("1" if c == "#" else "0" for c in diagram_str[::-1]), 2)
                buttons = [sum(2**v for v in map(int, btn[1:-1].split(","))) for btn in buttons_str.split(" ")]
                joltage = list(map(int, joltage_str.split(",")))
                machines.append((diagram, buttons, joltage))
    return machines


def read_input_part_B(input_filename: str) -> List[Machine]:
    machines: List[Machine] = []
    with open(input_filename, "r") as file:
        for line in file.read().splitlines():
            if res := PATTERN.findall(line):
                _, buttons_str, joltage_str = res[0]
                buttons = [list(map(int, btn[1:-1].split(","))) for btn in buttons_str.split(" ")]
                joltage = list(map(int, joltage_str.split(",")))
                machines.append((0, buttons, joltage))
    return machines


def process_machine(machine: IntMachine) -> int:
    diagram, buttons, _ = machine
    if diagram == 0:
        return 0

    if diagram in buttons:
        return 1

    visited = set(buttons)
    current_level = set(buttons)
    steps = 1

    while current_level:
        steps += 1
        next_level = set()
        for val in current_level:
            for but in buttons:
                new_val = val ^ but
                if new_val == diagram:
                    return steps
                if new_val not in visited:
                    visited.add(new_val)
                    next_level.add(new_val)
        current_level = next_level

    return 0


def solve_machine(machine: Machine) -> int:
    diagram, buttons, joltage = machine
    solver = Optimize()
    variables = [Int(f"x_{i}") for i in range(len(buttons))]
    for x in variables:
        solver.add(x >= 0)

    for j, voltage in enumerate(joltage):
        expr = None
        for i, but in enumerate(buttons):
            if j in but:
                if expr is None:
                    expr = variables[i]
                else:
                    expr = expr + variables[i]
        solver.add(expr == voltage)

    solver.minimize(sum(variables))

    if solver.check():
        model = solver.model()
        return sum(model.evaluate(v).as_long() for v in variables)  # type: ignore

    return 0


def part_A(input_filename: str) -> int:
    machines = read_input(input_filename)
    return sum(process_machine(machine) for machine in machines)


def part_B(input_filename: str) -> int:
    machines = read_input_part_B(input_filename)
    return sum(solve_machine(machine) for machine in machines)


def main() -> None:
    download_input(DAY, 2025)
    input_filename = f"day_{DAY}_input_sample.txt"
    input_filename = f"day_{DAY}_input.txt"

    with aoc_perf(memory=False):
        print(f"Day {DAY} Part A")
        answer = part_A(input_filename)
        print(f"Answer: {answer}")
        # Answer: 475

    with aoc_perf(memory=False):
        print(f"Day {DAY} Part B")
        answer = part_B(input_filename)
        print(f"Answer: {answer}")
        # Answer: 18273


if __name__ == "__main__":
    main()
