"""
Advent of Code 2024

https://adventofcode.com/2024/day/24

"""

import re
from typing import Any, Callable, Dict, List

from aoc_performance import aoc_perf
from aoc_utils import download_input

DAY = "24"


def read_input(input_filename: str) -> Dict:
    elems: Dict = {}
    with open(input_filename, "r") as file:
        consts, logics = file.read().split("\n\n")
        for const in consts.split("\n"):
            elem, value = const.split(": ")
            elems.setdefault(elem, {"value": int(value)})
        for logic in logics.split("\n"):
            if res := re.match(r"(\w+) (\w+) (\w+) -> (\w+)", logic):
                left, op, right, elem = res.groups()
                elems.setdefault(elem, {"left": left, "op": op, "right": right, "value": None})
    return elems


def get_value(elem: str, elems: Dict) -> int:
    if elems[elem]["value"] is not None:
        return elems[elem]["value"]
    left = elems[elem]["left"]
    right = elems[elem]["right"]
    if elems[elem]["op"] == "AND":
        elems[elem]["value"] = get_value(left, elems) and get_value(right, elems)
    elif elems[elem]["op"] == "OR":
        elems[elem]["value"] = get_value(left, elems) or get_value(right, elems)
    elif elems[elem]["op"] == "XOR":
        elems[elem]["value"] = get_value(left, elems) ^ get_value(right, elems)
    return elems[elem]["value"]


def part_A(input_filename: str) -> int:
    elems = read_input(input_filename)
    all_z = sorted([elem for elem in elems if elem.startswith("z")])
    bin_string = "".join([str(get_value(elem, elems)) for elem in reversed(all_z)])
    return int(bin_string, 2)


def part_B(input_filename: str) -> int:
    return 0


def main() -> None:
    download_input(DAY, 2024)
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
