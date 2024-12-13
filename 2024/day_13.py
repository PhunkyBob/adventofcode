"""
Advent of Code 2024
--- Day 13: Claw Contraption ---
https://adventofcode.com/2024/day/13

Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

This list describes the button configuration and prize location of claw machine.
"""

import contextlib
from typing import List, Tuple
import numpy as np
from aoc_performance import aoc_perf
import re

DAY = "13"

ClawMachine = Tuple[int, int, int, int, int, int]


def read_input(input_filename: str) -> List[ClawMachine]:
    with open(input_filename, "r") as file:
        return [get_params_from_claw_machine(claw_machine) for claw_machine in file.read().split("\n\n")]


def get_params_from_claw_machine(claw_machine: str) -> ClawMachine:
    line_A, line_B, line_prize = claw_machine.splitlines()
    pattern = re.compile(r"Button .: X\+(\d+), Y\+(\d+)")
    a_x, a_y = extract_values(pattern, line_A)
    b_x, b_y = extract_values(pattern, line_B)
    pattern = re.compile(r"Prize: X=(\d+), Y=(\d+)")
    res_x, res_y = extract_values(pattern, line_prize)
    return a_x, a_y, b_x, b_y, res_x, res_y


def extract_values(pattern, text):
    result = re.match(pattern, text)
    if result is None:
        raise ValueError("Invalid input")
    x, y = map(int, result.groups())
    return x, y


def solve_equations_numpy(a_x: int, b_x: int, res_x: int, a_y: int, b_y: int, res_y: int) -> tuple[int, int]:
    """
    Solves the system of equations:
    a_x * a + b_x * b = res_x
    a_y * a + b_y * b = res_y
    """
    A = np.array([[a_x, b_x], [a_y, b_y]])
    b = np.array([res_x, res_y])

    try:
        solution = np.linalg.solve(A, b)
        answer_A, answer_B = int(round(solution[0])), int(round(solution[1]))
        if (a_x * answer_A + b_x * answer_B) != res_x or (a_y * answer_A + b_y * answer_B) != res_y:
            raise ValueError("No integer solution")
        return answer_A, answer_B
    except np.linalg.LinAlgError as e:
        raise ValueError("No unique solution") from e


def part_A(input_filename: str) -> int:
    price_A: int = 3
    price_B: int = 1
    claw_machines: List[ClawMachine] = read_input(input_filename)
    total_cost = 0
    for claw_machine in claw_machines:
        a_x, a_y, b_x, b_y, res_x, res_y = claw_machine
        with contextlib.suppress(ValueError):
            a, b = solve_equations_numpy(a_x, b_x, res_x, a_y, b_y, res_y)
            if 0 <= a <= 100 and 0 <= b <= 100:
                total_cost += a * price_A + b * price_B
    return total_cost


def part_B(input_filename: str) -> int:
    price_A: int = 3
    price_B: int = 1
    claw_machines: List[ClawMachine] = read_input(input_filename)
    total_cost = 0
    for claw_machine in claw_machines:
        a_x, a_y, b_x, b_y, res_x, res_y = claw_machine
        res_x = res_x + 10000000000000
        res_y = res_y + 10000000000000
        with contextlib.suppress(ValueError):
            a, b = solve_equations_numpy(a_x, b_x, res_x, a_y, b_y, res_y)
            total_cost += a * price_A + b * price_B
    return total_cost


def main() -> None:
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
