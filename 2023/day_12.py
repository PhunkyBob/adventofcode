"""
Advent of Code 2023
--- Day 12: Hot Springs ---
https://adventofcode.com/2023/day/12

However, the condition records are partially damaged; some of the springs' conditions are actually unknown (?). For example:

???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1

"""
from functools import lru_cache
from typing import List, Tuple
from aoc_performance import aoc_perf
import re

DAY = "12"


def count_possible_regex(input: str, pattern: str) -> int:
    new_pattern = r"(\.|\?)+".join([r"(#|\?)" * int(i) for i in pattern.split(",")])
    new_pattern = r"^(\.|\?)*" + new_pattern + r"(\.|\?)*$"
    if re.match(new_pattern, input):
        if "?" in input:
            return count_possible_regex(input.replace("?", ".", 1), pattern) + count_possible_regex(
                input.replace("?", "#", 1), pattern
            )
        else:
            # print(input)
            return 1
    return 0


def read_input(input_filename: str) -> List[Tuple[str, ...]]:
    with open(input_filename, "r") as input_file:
        return [tuple(line.strip().split(" ")) for line in input_file]


def part_A(input_filename: str) -> int:
    data = read_input(input_filename)
    # return sum(count_possible_regex(d[0], d[1]) for d in data)
    return sum(count_possible_part2(springs_to_tuple(d[0], False), size_to_tuple(d[1], False)) for d in data)


def unfold(input: str, separator: str, times: int = 5) -> str:
    return separator.join([input] * times)


def springs_to_tuple(sequence: str, apply_unfold: bool = False) -> Tuple[str, ...]:
    if apply_unfold:
        sequence = unfold(sequence, "?")
    return tuple(elem for elem in sequence.split(".") if elem)


def size_to_tuple(sequence: str, apply_unfold: bool = False) -> Tuple[int, ...]:
    if apply_unfold:
        sequence = unfold(sequence, ",")
    return tuple(int(elem) for elem in sequence.split(",") if elem)


@lru_cache
def is_possible(spring: str, size: int) -> bool:
    pattern = r"^[#|\?]{" + str(size) + "}" + r"(\?|$)"
    return re.match(pattern, spring) is not None


@lru_cache
def count_possible_part2(springs: Tuple[str, ...], sizes: Tuple[int, ...]) -> int:
    if not sizes:
        return 1 if all(spring.replace("?", "") == "" for spring in springs) else 0
    if not springs:
        return 0

    first_spring = springs[0]
    if not first_spring:
        return count_possible_part2(springs[1:], sizes)

    if first_spring[0] == "#":
        return (
            count_possible_part2((first_spring[sizes[0] + 1 :],) + springs[1:], sizes[1:])
            if is_possible(first_spring, sizes[0])
            else 0
        )
    # else char == "?":
    res_when_empty = count_possible_part2((first_spring[1:],) + springs[1:], sizes)
    res_when_broken = count_possible_part2((f"#{first_spring[1:]}",) + springs[1:], sizes)
    return res_when_empty + res_when_broken


def part_B(input_filename: str) -> int:
    data = read_input(input_filename)
    return sum(count_possible_part2(springs_to_tuple(d[0], True), size_to_tuple(d[1], True)) for d in data)


def main() -> None:
    input_filename = f"day_{DAY}_input.txt"
    # input_filename = f"day_{DAY}_input_sample.txt"

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
