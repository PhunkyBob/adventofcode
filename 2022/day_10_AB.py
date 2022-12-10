# -*- coding: utf-8 -*-
""" 
--- Day 10: Cathode-Ray Tube ---
https://adventofcode.com/2022/day/10


"""
DAY = "10"

from aoc_performance import aoc_perf
from typing import Tuple


def get_instruction(line: str) -> Tuple[int, int]:
    """Returns cycles_to_wait, value_to_add."""
    if line.strip() == "noop":
        return 1, 0
    _, value_to_add = line.split(" ")
    return 2, int(value_to_add)


def is_key_cycle(cycle: int) -> bool:
    START = 20
    MOD = 40
    return cycle == START or (cycle - START) % MOD == 0


def get_signal_strength(filename: str) -> Tuple[int, int]:
    x = 1
    cycle = 0
    with open(filename, "r") as f:
        for line in f:
            cycles_to_wait, value_to_add = get_instruction(line)
            for _ in range(cycles_to_wait):
                cycle += 1
                if is_key_cycle(cycle):
                    yield cycle, x
            x += value_to_add


def is_print_pixel(cycle: int, x: int) -> bool:
    return abs(cycle - 1 - x) <= 1


def print_sprite_position(x: int) -> None:
    print(f"Sprite position:", "".join(["#" if abs(i - x) <= 1 else "." for i in range(40)]))


def print_sprites(filename: str, debug=False) -> None:
    LINE_WIDTH = 40
    x = 1
    cycle = 0
    with open(filename, "r") as f:
        current_crt_row = ""
        for line in f:
            cycles_to_wait, value_to_add = get_instruction(line)
            for _ in range(cycles_to_wait):
                cycle += 1
                pixel = "#" if is_print_pixel(cycle, x) else "."

                if debug:
                    current_crt_row += pixel
                    print(f"During cycle  {cycle}: CRT draws pixel in position {cycle-1}")
                    print(f"Current CRT row: {current_crt_row}")
                else:
                    print(pixel, end="")
                if cycle % LINE_WIDTH == 0:
                    cycle = 0
                    if debug:
                        current_crt_row = ""
                    else:
                        print()
            x += value_to_add
            if debug:
                print(f"End of cycle  {cycle}: finish executing addx {value_to_add} (Register X is now {x})")
                print_sprite_position(x)


def part_one(filename: str) -> int:
    total_strength = 0
    for cycle, value in get_signal_strength(filename):
        total_strength += cycle * value
    return total_strength


def part_two(filename: str) -> None:
    print_sprites(filename, False)
    return


def main() -> None:
    # input_filename = f"day_{DAY}_input_sample.txt"
    input_filename = f"day_{DAY}_input_sample2.txt"
    input_filename = f"day_{DAY}_input.txt"

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
