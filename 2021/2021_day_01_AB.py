# https://adventofcode.com/2021/day/1

import time

if __name__ == '__main__':
    start_time = time.time()

    input_file = '2021_day_01_input_sample.txt'
    input_file = '2021_day_01_input.txt'
    input = [int(x) for x in open(input_file, 'r').readlines()]

    """Part One"""
    result = sum([1 if input[i] > input[i-1] else 0 for i in range(1, len(input))])
    print(f'Day 01 Part One: {result}')

    """Part Two"""
    cumulative_input = [input[i] + input[i-1] + input[i-2] for i in range(2, len(input))]
    result = sum([1 if cumulative_input[i] > cumulative_input[i-1] else 0 for i in range(1, len(cumulative_input))])
    print(f'Day 01 Part Two: {result}')
    print("--- %.2f seconds ---" % (time.time() - start_time))

