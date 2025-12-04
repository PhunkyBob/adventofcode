import re
from typing import Dict

from aoc_utils import download_input
from day_03 import DAY

MAP_DIGITS: Dict[str, str] = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def get_first_and_last_re_part_A(text: str) -> int:
    res = re.findall(r"\d", text)
    return int(res[0] + res[-1])


def get_first_and_last_re_part_B(text: str) -> int:
    res = re.findall(r"(?=(\d|" + "|".join(MAP_DIGITS.keys()) + "))", text)
    return int(MAP_DIGITS.get(res[0], res[0]) + MAP_DIGITS.get(res[-1], res[-1]))


download_input(DAY, 2023)
input_filename = "day_01_input.txt"
answer = sum(map(get_first_and_last_re_part_A, open(input_filename, "r")))
print(f"Day 01 Part A: {answer}")

answer = sum(map(get_first_and_last_re_part_B, open(input_filename, "r")))
print(f"Day 01 Part B: {answer}")
