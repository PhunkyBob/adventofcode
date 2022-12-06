# -*- coding: utf-8 -*-
""" https://adventofcode.com/2021/day/16 """

import time

def load_input(filename):
    return [x.strip() for x in open(filename, 'r').readlines()]


def solve_part_one(input):
    return 


if __name__ == '__main__':
    start_time = time.time()

    input_file = '2021_day_16_input_sample.txt'
    # input_file = '2021_day_16_input.txt'
    input = load_input(input_file)

    """Part One"""
    result = solve_part_one(input)
    print(f'Day 16 Part One: {result}')

    """Part Two"""
    print(f'Day 16 Part Two: {result}')

    print("--- %.2f seconds ---" % (time.time() - start_time))

