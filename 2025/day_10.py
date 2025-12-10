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
from typing import Dict, List, Tuple

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


def read_input(input_filename: str) -> List[IntMachine]:
    machines: List[IntMachine] = []
    with open(input_filename, "r") as file:
        for line in file.read().splitlines():
            if res := re.findall(r"\[([\.#]+)\] (.+) \{([\d,]+)\}", line):
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
            if res := re.findall(r"\[([\.#]+)\] (.+) \{([\d,]+)\}", line):
                _, buttons_str, joltage_str = res[0]
                buttons = [list(map(int, btn[1:-1].split(","))) for btn in buttons_str.split(" ")]
                joltage = list(map(int, joltage_str.split(",")))
                machines.append((0, buttons, joltage))
    return machines


def press_button(diagram: Diagram, button: IntButton) -> Diagram:
    return diagram ^ button


def process_machine(machine: IntMachine) -> int:
    diagram, buttons, joltage = machine
    values: Dict[int, List[IntButton]] = {but: [but] for but in buttons}

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
