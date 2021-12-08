# -*- coding: utf-8 -*-
""" https://adventofcode.com/2021/day/7 """

import time


def load_input(filename):
    return [int(x) for x in open(filename, "r").read().strip().split(",")]


def solve_part_one(input, method="constant"):
    move_to_cost = {}
    move_from = min(input)
    move_to = max(input)
    for i in range(move_from, move_to + 1):
        cost = sum([calc_cost(abs(x - i), method) for x in input])
        move_to_cost[i] = cost

    min_cost = min(move_to_cost.values())
    # move_to_position = [k for k, v in move_to_cost.items() if v == min_cost]
    return min_cost


def calc_cost(dist, method="constant"):
    if method == "constant":
        return dist
    else:
        return dist * (dist + 1) // 2


def solve_part_two(input):
    return solve_part_one(input, method="more and more expensive")


if __name__ == "__main__":
    start_time = time.time()

    # input_file = '2021_day_07_input_sample.txt'
    input_file = "2021_day_07_input.txt"
    input = load_input(input_file)

    """Part One"""
    result = solve_part_one(input)
    print(f"Day X Part One: {result}")
    # Your puzzle answer was 335330.

    """Part Two"""
    result = solve_part_two(input)
    print(f"Day X Part Two: {result}")
    # Your puzzle answer was 92439766.

    print("--- %.2f seconds ---" % (time.time() - start_time))
