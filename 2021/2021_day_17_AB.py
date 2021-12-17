# -*- coding: utf-8 -*-
""" https://adventofcode.com/2021/day/17 """

import time
import re
from itertools import product


def get_range(input):
    res = re.search(r"target area: x=([\d-]+)..([\d-]+), y=([\d-]+)..([\d-]+)", input)
    range_x_min, range_x_max, range_y_min, range_y_max = res.groups()
    range_x = (
        min(int(range_x_min), int(range_x_max)),
        max(int(range_x_min), int(range_x_max)),
    )
    range_y = (
        min(int(range_y_min), int(range_y_max)),
        max(int(range_y_min), int(range_y_max)),
    )
    return range_x, range_y


def get_next_step(pos_x, pos_y, x, y):
    new_pos_x, new_pos_y = pos_x + x, pos_y + y
    new_x = x
    if x > 0:
        new_x -= 1
    elif x < 0:
        new_x += 1
    else:
        new_x = 0
    new_y = y - 1
    return pos_x + x, pos_y + y, new_x, new_y


def is_valid(pos_x, pos_y, range_x, range_y):
    return (
        pos_x >= range_x[0]
        and pos_x <= range_x[1]
        and pos_y >= range_y[0]
        and pos_y <= range_y[1]
    )


def is_too_far(pos_x, pos_y, range_x, range_y):
    return pos_x > range_x[1] or pos_y < range_y[0]


def get_possible_velocities(range_x, range_y):
    velocity_ok = {}
    for x, y in product(
        range(0, range_x[1] + 1, int(abs(range_x[1] / range_x[1]))),
        range(range_y[0] - 1, 0 - range_y[0]),
    ):
        vel_x, vel_y = x, y
        max_y = 0
        pos_x, pos_y = 0, 0
        target_ok = False
        while not is_too_far(pos_x, pos_y, range_x, range_y) and not target_ok:
            if is_valid(pos_x, pos_y, range_x, range_y):
                target_ok = True
                velocity_ok[(x, y)] = max_y
                continue
            pos_x, pos_y, vel_x, vel_y = get_next_step(pos_x, pos_y, vel_x, vel_y)
            max_y = max(max_y, pos_y)
    return velocity_ok


def solve_part_one(input):
    range_x, range_y = get_range(input)
    velocity_ok = get_possible_velocities(range_x, range_y)
    return max(list(velocity_ok.values()))


def solve_part_two(input):
    range_x, range_y = get_range(input)
    velocity_ok = get_possible_velocities(range_x, range_y)
    return len(velocity_ok)


if __name__ == "__main__":
    start_time = time.time()

    # input = "target area: x=20..30, y=-10..-5"
    input = "target area: x=70..125, y=-159..-121"

    """Part One"""
    result = solve_part_one(input)
    print(f"Day 17 Part One: {result}")

    """Part Two"""
    result = solve_part_two(input)
    print(f"Day 17 Part Two: {result}")

    print("--- %.2f seconds ---" % (time.time() - start_time))
