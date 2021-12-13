# -*- coding: utf-8 -*-
""" https://adventofcode.com/2021/day/13 """

import time


def load_input(filename):
    dots = {}
    with open(filename, "r") as f:
        dots_txt, actions = f.read().split("\n\n")
    return (
        {(x, y): True for x, y in [list(map(int, x.split(","))) for x in dots_txt.split("\n")]},
        list(
            map(lambda x: x.replace("fold along ", "").split("="), actions.split("\n"))
        )
    )


def fold_along(dots, axis, position):
    new_dots = {}
    for dot in dots:
        if axis == "y":
            if dot[1] < position:
                new_dots[(dot[0], dot[1])] = True
            else:
                new_dots[(dot[0], position - dot[1] + position)] = True
        elif axis == "x":
            if dot[0] < position:
                new_dots[(dot[0], dot[1])] = True
            else:
                new_dots[(position - dot[0] + position, dot[1])] = True
    return new_dots


def display(dots, empty=".", filled="#"):
    min_x = min(dots, key=lambda x: x[0])[0]
    max_x = max(dots, key=lambda x: x[0])[0]
    min_y = min(dots, key=lambda x: x[1])[1]
    max_y = max(dots, key=lambda x: x[1])[1]

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x, y) in dots:
                print(filled, end="")
            else:
                print(empty, end="")
        print()


def solve_part_one(dots, actions):
    # display(dots)
    new_dots = fold_along(dots, actions[0][0], int(actions[0][1]))
    # print()
    # display(new_dots)
    return len(new_dots)


def solve_part_two(dots, actions):
    new_dots = dots
    # display(new_dots)
    for action in actions:
        new_dots = fold_along(new_dots, action[0], int(action[1]))
        # print()
        # display(new_dots)
    display(new_dots, " ", "▮")
    return


if __name__ == "__main__":
    start_time = time.time()

    input_file = '2021_day_13_input_sample.txt'
    input_file = "2021_day_13_input.txt"
    dots, actions = load_input(input_file)

    """Part One"""
    result = solve_part_one(dots, actions)
    print(f"Day 13 Part One: {result}")
    # Your puzzle answer was 942.

    """Part Two"""
    print(f"Day 13 Part Two: ")
    solve_part_two(dots, actions)
    # Your puzzle answer was JZGUAPRB.

    print("--- %.2f seconds ---" % (time.time() - start_time))
