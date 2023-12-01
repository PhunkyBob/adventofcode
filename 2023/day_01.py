"""
Advent of Code 2023
--- Day 1: Trebuchet?! ---
https://adventofcode.com/2023/day/1

On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.
"""
from typing import Any, Callable, List
from aoc_performance import aoc_perf
from aoc_utils import compose
import re

DAY = "01"
MAP_DIGITS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}


def replace_digits(text: str) -> str:
    for digit in MAP_DIGITS:
        text = text.replace(digit, f"{digit}{MAP_DIGITS[digit]}{digit}")
    return text


def keep_only_digits(text: str) -> str:
    return "".join(filter(str.isdigit, text))


def get_first_and_last(text: str) -> str:
    return f"{text[0]}{text[-1]}" if text else ""


def read_input(filename: str, transformations: Callable = lambda x: x) -> List[int]:
    data: List[int] = []
    with open(filename, "r") as f:
        data = list(map(transformations, f.readlines()))
    return data


def get_first_and_last_re(text: str) -> str:
    res = re.findall(r"\d+", text)
    return res[0] + res[-1]


def get_first_and_last_re_part_B(text: str) -> str:
    res = re.findall(r"(?=(\d+|" + "|".join(MAP_DIGITS.keys()) + "))", text)
    return f"{MAP_DIGITS.get(res[0], res[0])}{MAP_DIGITS.get(res[-1], res[-1])}"


def part_A(input_filename: str) -> int:
    # data: List[int] = read_input(input_filename, compose(keep_only_digits, get_first_and_last, int))
    data: List[int] = read_input(input_filename, compose(get_first_and_last_re, int))
    return sum(data)


def part_B(input_filename: str) -> int:
    # data: List[int] = read_input(input_filename, compose(replace_digits, keep_only_digits, get_first_and_last, int))
    data: List[int] = read_input(input_filename, compose(get_first_and_last_re_part_B, int))
    return sum(data)


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
