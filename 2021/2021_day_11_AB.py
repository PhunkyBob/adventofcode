# -*- coding: utf-8 -*-
""" https://adventofcode.com/2021/day/11 """

import time
from itertools import product


class Octopus:
    cavern = []

    def __init__(self, input_file):
        self.cavern = [
            [int(y) for y in list(x.strip())] for x in open(input_file, "r").readlines()
        ]

    def increase(self, x, y):
        self.cavern[y][x] += 1
        if self.cavern[y][x] == 10:
            for dy, dx in product(range(-1, 2), repeat=2):
                if (
                    (dx, dy) != (0, 0)
                    and y + dy >= 0
                    and y + dy < len(self.cavern)
                    and x + dx >= 0
                    and x + dx < len(self.cavern[y + dy])
                ):
                    self.increase(x + dx, y + dy)

    def increase_all(self):
        for y, x in product(range(len(self.cavern)), range(len(self.cavern[0]))):
            self.increase(x, y)

        # self.cavern = [[0 if val >= 10 else val for val in line] for line in self.cavern]
        # flashed = sum([sum([1 if val == 0 else 0 for val in line]) for line in self.cavern])

        flashed = 0
        for y, x in product(range(len(self.cavern)), range(len(self.cavern[0]))):
            if self.cavern[y][x] >= 10:
                self.cavern[y][x] = 0
                flashed += 1

        return flashed

    def is_synced(self):
        return sum([sum(y) for y in self.cavern]) == 0

    def display(self):
        for y in self.cavern:
            print("".join([str(x) for x in y]))
        print()


def solve_part_one(input_file):
    input = Octopus(input_file)
    # input.display()
    total_flashes = 0
    for i in range(100):
        # print(f"Step {i+1} : ")
        total_flashes += input.increase_all()
        # input.display()
    return total_flashes


def solve_part_two(input_file):
    input = Octopus(input_file)
    rounds = 0
    while input.is_synced() == False:
        # print(f"Step {rounds+1} : ")
        input.increase_all()
        # input.display()
        rounds += 1

    return rounds


if __name__ == "__main__":
    start_time = time.time()

    # input_file = "2021_day_11_input_sample.txt"
    # input_file = "2021_day_11_input_sample2.txt"
    input_file = "2021_day_11_input.txt"

    """Part One"""
    result = solve_part_one(input_file)
    print(f"Day 11 Part One: {result}")
    # Your puzzle answer was 1585.

    """Part Two"""
    result = solve_part_two(input_file)
    print(f"Day 11 Part Two: {result}")
    # Your puzzle answer was 382.

    print("--- %.2f seconds ---" % (time.time() - start_time))
