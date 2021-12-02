# -*- coding: utf-8 -*-
""" https://adventofcode.com/2021/day/1 """

import time

def solve_part_one(input):
    return sum([1 if input[i] > input[i-1] else 0 for i in range(1, len(input))])

def solve_part_one_and_two(input, window_size=1):
    return sum([1 if sum(input[i-window_size+1:i+1]) > sum(input[i-window_size:i]) else 0 for i in range(window_size, len(input))])


if __name__ == '__main__':
    start_time = time.time()

    # input_file = '2021_day_01_input_sample.txt'
    input_file = '2021_day_01_input.txt'
    input = [int(x) for x in open(input_file, 'r').readlines()]

    """Part One"""
    # result = solve_part_one(input)
    result = solve_part_one_and_two(input)
    print(f'Day 01 Part One: {result}')

    """Part Two"""
    

    # # Version avec recyclage de la fonction de la partie 1 : 
    # cumulative_input = [sum(input[i-window_size+1:i+1]) for i in range(2, len(input))]
    # result = solve_part_one(cumulative_input)

    # Version optimisée sans création de tableau intermédiaire : 
    result = solve_part_one_and_two(input, window_size=3)
    print(f'Day 01 Part Two: {result}')

    print("--- %.2f seconds ---" % (time.time() - start_time))

