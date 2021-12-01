# -*- coding: utf-8 -*-
""" https://adventofcode.com/2021/day/1 """

import time

def process(input):
    return sum([1 if input[i] > input[i-1] else 0 for i in range(1, len(input))])


if __name__ == '__main__':
    start_time = time.time()

    input_file = '2021_day_01_input_sample.txt'
    input_file = '2021_day_01_input.txt'
    input = [int(x) for x in open(input_file, 'r').readlines()]

    """Part One"""
    result = process(input)
    print(f'Day 01 Part One: {result}')

    """Part Two"""
    cumulative_input = [input[i] + input[i-1] + input[i-2] for i in range(2, len(input))]
    result = process(cumulative_input)
    print(f'Day 01 Part Two: {result}')

    print("--- %.2f seconds ---" % (time.time() - start_time))

