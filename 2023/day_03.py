"""
Advent of Code 2023
--- Day 3: Gear Ratios ---
https://adventofcode.com/2023/day/3


The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.
"""
from typing import List, Tuple
from aoc_performance import aoc_perf
from dataclasses import dataclass


DAY = "03"


@dataclass
class Number:
    value: int
    x: int
    y: int

    @property
    def x_max(self) -> int:
        return self.x + len(str(self.value)) - 1


@dataclass
class Symbol:
    value: str
    x: int
    y: int


def read_file(filename: str) -> List[List[str]]:
    return [list(line.strip()) for line in open(filename, "r")]


def convert(data: List[List[str]]) -> Tuple[List[Number], List[Symbol]]:
    numbers = []
    symbols = []
    for y, line in enumerate(data):
        x = 0
        while x < len(line):
            c = data[y][x]
            if c.isdigit():
                digits: str = ""
                while c.isdigit():
                    digits += c
                    x += 1
                    c = data[y][x] if x < len(data[y]) else "."
                numbers.append(Number(int(digits), x - len(digits), y))
            if c != ".":
                symbols.append(Symbol(c, x, y))
            x += 1
    return numbers, symbols


def get_numbers_near_symbol(numbers: List[Number], symbols: List[Symbol]) -> List[int]:
    near: List[int] = []
    for symbol in symbols:
        near += [n.value for n in numbers if n.x - 1 <= symbol.x <= n.x_max + 1 and abs(n.y - symbol.y) <= 1]
    return near


def get_gear_ratio(numbers: List[Number], symbols: List[Symbol]) -> int:
    total_gear_ratio = 0
    for symbol in symbols:
        if symbol.value != "*":
            continue
        near = [n.value for n in numbers if n.x - 1 <= symbol.x <= n.x_max + 1 and abs(n.y - symbol.y) <= 1]
        if len(near) == 2:
            total_gear_ratio += near[0] * near[1]
    return total_gear_ratio


def part_A(input_filename: str) -> int:
    data = read_file(input_filename)
    numbers, symbols = convert(data)
    near = get_numbers_near_symbol(numbers, symbols)
    return sum(near)


def part_B(input_filename: str) -> int:
    data = read_file(input_filename)
    numbers, symbols = convert(data)
    return get_gear_ratio(numbers, symbols)


def main() -> None:
    input_filename = f"day_{DAY}_input.txt"

    with aoc_perf(memory=True):
        print(f"Day {DAY} Part A")
        answer = part_A(input_filename)
        print(f"Answer: {answer}")

    with aoc_perf(memory=True):
        print(f"Day {DAY} Part B")
        answer = part_B(input_filename)
        print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
