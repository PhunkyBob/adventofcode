# -*- coding: utf-8 -*-
""" https://adventofcode.com/2021/day/4 """

import time

class Bingo:
    numbers = []
    grids = []

    def __init__(self, filename) -> None:
        with open(filename) as f:
            numbers, *grids = f.read().split("\n\n")
            self.numbers = [int(x) for x in numbers.split(",")]
            self.grids = [Grid(x) for x in grids]
        return

    def draw_until_first_win(self):
        for number in self.numbers:
            for grid in self.grids:
                is_bingo = grid.draw(number)
                if is_bingo:
                    return grid.sum_remaining() * number
        return False

    def draw_until_last_win(self):
        for number in self.numbers:
            for i in reversed(range(len(self.grids))):
                grid = self.grids[i]
                is_bingo = grid.draw(number)
                if is_bingo:
                    if len(self.grids) == 1:
                        return self.grids[0].sum_remaining() * number
                    del self.grids[i]
        return False


class Grid:
    values = []
    CHECKED_VALUE: str = ""

    def __init__(self, text_content) -> None:
        self.values = [
            [int(val) for val in line.split()] for line in text_content.split("\n")
        ]
        return

    def draw(self, number):
        for i in range(len(self.values)):
            for j in range(len(self.values[i])):
                if self.values[i][j] == number:
                    self.values[i][j] = self.CHECKED_VALUE
        return self.check_if_bingo()

    def check_if_empty(self, line):
        return all(i == self.CHECKED_VALUE for i in line)

    def check_if_bingo(self):
        bingo_line = any(self.check_if_empty(l) for l in self.values)
        bingo_column = any(self.check_if_empty(l) for l in zip(*self.values))
        return bingo_line or bingo_column

    def sum_remaining(self):
        return sum(
            sum(i for i in line if i != self.CHECKED_VALUE) for line in self.values
        )


def solve_part_one(bingo):
    bingo = Bingo(input_file)
    res = bingo.draw_until_first_win()
    return res


def solve_part_two(bingo):
    bingo = Bingo(input_file)
    res = bingo.draw_until_last_win()
    return res


if __name__ == "__main__":
    start_time = time.time()

    # input_file = "2021_day_04_input_sample.txt"
    input_file = "2021_day_04_input.txt"

    """Part One"""
    result = solve_part_one(input_file)
    print(f"Day 4 Part One: {result}")

    """Part Two"""
    result = solve_part_two(input_file)
    print(f"Day 4 Part Two: {result}")

    print("--- %.2f seconds ---" % (time.time() - start_time))
