# -*- coding: utf-8 -*-
""" https://adventofcode.com/2022/day/5 """
DAY = "05"

from aoc_performance import aoc_perf
from dataclasses import dataclass
import re
from typing import List


@dataclass
class Movment:
    move: int
    m_from: int
    m_to: int


def process_stacks(stacks_txt: str) -> dict:
    lines = stacks_txt.split("\n")[::-1]
    stacks = {int(stack_no): [] for stack_no in lines[0].split()}
    for line in lines[1:]:
        for i in range(len(stacks)):
            idx = i * 4 + 1
            if idx >= len(line):
                continue
            elem = line[idx]
            if elem.strip():
                stacks[i + 1].append(elem)
    return stacks


def process_instructions(instructions_txt: str) -> List[Movment]:
    instructions = []
    for line in instructions_txt.strip().split("\n"):
        move, m_from, m_to = map(int, re.match(r"move (\d+) from (\d+) to (\d+)", line).groups())
        instructions.append(Movment(move, m_from, m_to))
    return instructions


def read_input(filename: str):
    with open(filename, "r") as f:
        all_txt = f.read()
        stacks_txt, instructions_txt = all_txt.split("\n\n")
    return process_stacks(stacks_txt), process_instructions(instructions_txt)


def print_stacks(stacks) -> None:
    for k, val in stacks.items():
        print(f"{k} : {val}")


def read_tops(stacks) -> str:
    return "".join([val[-1] for val in stacks.values() if val])


def part_one(filename: str, model: str = "9000") -> int:
    stacks, instructions = read_input(filename)
    for instruction in instructions:
        elems = []
        for _ in range(instruction.move):
            elems.append(stacks[instruction.m_from].pop())
        if model == "9001":
            elems.reverse()
        stacks[instruction.m_to] += elems
        # print_stacks(stacks)
    return read_tops(stacks)


def part_two(filename: str) -> int:
    return part_one(filename, model="9001")


def main() -> None:
    input_filename = f"2022_day_{DAY}_input_sample.txt"
    input_filename = f"2022_day_{DAY}_input.txt"

    with aoc_perf():
        print(f"Day {DAY} Part One")
        answer = part_one(input_filename)
        print(f"Answer: {answer}")

    with aoc_perf():
        print(f"Day {DAY} Part Two")
        answer = part_two(input_filename)
        print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
