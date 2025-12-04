"""
Advent of Code 2024
--- Day 17: Chronospatial Computer ---
https://adventofcode.com/2024/day/17

"""

from itertools import batched
from typing import Any, Callable, Dict, List, Optional
import re
from aoc_performance import aoc_perf
from aoc_utils import download_input

DAY = "17"


class Computer:
    register_a: int
    register_b: int
    register_c: int
    program: List[int]
    instruction_pointer: int
    outputs: List[int]

    def __init__(self, source: str = "") -> None:
        self.register_a = 0
        self.register_b = 0
        self.register_c = 0
        self.program = []
        if source:
            self.read_from_file(source)

    def read_from_file(self, source: str) -> None:
        with open(source, "r") as file:
            data = file.read()
            self.register_a, self.register_b, self.register_c = list(map(int, re.findall(r"Register .: (\d+)", data)))
            self.program = [int(x) for x in re.findall(r"(\d+)", data.split("\n")[-1])]

    def run(self, target: Optional[List[int]] = None) -> List[int]:
        self.instruction_pointer = 0
        self.outputs = []
        while self.instruction_pointer < len(self.program):
            # print(self)
            opcode = self.program[self.instruction_pointer]
            operand = self.program[self.instruction_pointer + 1]
            self.instruction_pointer += 2
            match opcode:
                case 0:
                    self.adv(operand)
                case 1:
                    self.bxl(operand)
                case 2:
                    self.bst(operand)
                case 3:
                    self.jnz(operand)
                case 4:
                    self.bxc()
                case 5:
                    self.out(operand)
                    if target and self.outputs != target[: len(self.outputs)]:
                        return self.outputs
                case 6:
                    self.bdv(operand)
                case 7:
                    self.cdv(operand)
                case _:
                    raise ValueError(f"Invalid opcode {opcode}")
        return self.outputs

    def adv(self, operand: int) -> None:
        self.register_a = int(self.register_a / (2 ** self.get_combo_operand(operand)))

    def bxl(self, operand: int) -> None:
        self.register_b = self.register_b ^ self.get_literal_operand(operand)

    def bst(self, operand: int) -> None:
        self.register_b = self.get_combo_operand(operand) % 8

    def jnz(self, operand: int) -> None:
        if self.register_a == 0:
            return
        self.instruction_pointer = self.get_literal_operand(operand)

    def bxc(self) -> None:
        self.register_b = self.register_b ^ self.register_c

    def out(self, operand: int) -> None:
        self.outputs.append(self.get_combo_operand(operand) % 8)

    def bdv(self, operand: int) -> None:
        self.register_b = int(self.register_a / (2 ** self.get_combo_operand(operand)))

    def cdv(self, operand: int) -> None:
        self.register_c = int(self.register_a / (2 ** self.get_combo_operand(operand)))

    def get_literal_operand(self, operand: int) -> int:
        return operand

    def get_combo_operand(self, operand: int) -> int:
        if 0 <= operand <= 3:
            return operand
        if operand == 4:
            return self.register_a
        if operand == 5:
            return self.register_b
        if operand == 6:
            return self.register_c
        raise ValueError(f"Invalid operand {operand}")

    def __repr__(self) -> str:
        return f"A={self.register_a}, B={self.register_b}, C={self.register_c}, {self.program}, IP={self.instruction_pointer}, outputs={self.outputs}"


def part_A(input_filename: str) -> str:
    cpu = Computer(input_filename)
    result = cpu.run()
    return ",".join(list(map(str, result)))


def part_B(input_filename: str) -> int:
    cpu = Computer(input_filename)
    candidate = 0
    cpu.register_a = candidate
    result = cpu.run()
    while result != cpu.program:
        if candidate % 1_000_000 == 0:
            print(f"Trying {candidate}")
        candidate += 1
        cpu.register_a = candidate
        cpu.register_b = 0
        cpu.register_c = 0
        result = cpu.run(cpu.program)
    return candidate


def main() -> None:
    download_input(DAY, 2024)
    input_filename = f"day_{DAY}_input_sample2.txt"
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
