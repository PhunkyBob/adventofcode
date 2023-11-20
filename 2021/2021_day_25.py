# -*- coding: utf-8 -*-
""" 

https://adventofcode.com/2021/day/25


"""
from copy import deepcopy

DAY = "25"


def read_input(filename: str):
    data = []
    with open(filename, "r") as f:
        data.extend(list(line) for line in map(lambda x: x.strip(), f))
    return data


def do_step(data: list) -> list:
    data_new = deepcopy(data)
    width = len(data[0])
    height = len(data)
    # Move east facing.
    for y, line in enumerate(data):
        for x, elem in enumerate(line):
            if elem != ">":
                continue
            next_x = (x + 1) % width
            if line[next_x] == ".":
                data_new[y][x] = "."
                data_new[y][next_x] = ">"
    data = deepcopy(data_new)
    # Move south facing.
    for y, line in enumerate(data):
        for x, elem in enumerate(line):
            if elem != "v":
                continue
            next_y = (y + 1) % height
            if data[next_y][x] == ".":
                data_new[y][x] = "."
                data_new[next_y][x] = "v"

    return data_new


def part_one(filename: str) -> int:
    new_data = read_input(filename)
    data = []
    cnt_step = 0
    while new_data != data:
        data = new_data
        new_data = do_step(data)
        cnt_step += 1

    return cnt_step


def main() -> None:
    input_filename = f"2021_day_{DAY}_input_sample.txt"
    input_filename = f"2021_day_{DAY}_input.txt"

    print(f"Day {DAY}")
    answer = part_one(input_filename)
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
