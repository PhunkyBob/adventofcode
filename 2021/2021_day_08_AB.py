# -*- coding: utf-8 -*-
""" https://adventofcode.com/2021/day/8 """

import time

def load_input(filename):
    return [[[elem for elem in part.split()] for part in x.strip().split(" | ")] for x in open(filename, 'r').readlines()]


def solve_part_one(input):
    res = sum(sum([1 for val in line[1] if len(val) in [2, 4, 3, 7]]) for line in input)
    return res

def solve_part_two(input):
    res = 0
    for line in input:
        digits = {}
        digits[1] = list([val for val in line[0] if len(val) == 2][0])
        digits[7] = list([val for val in line[0] if len(val) == 3][0])
        digits[4] = list([val for val in line[0] if len(val) == 4][0])
        digits[8] = list([val for val in line[0] if len(val) == 7][0])

        while len(digits) < 10:
            for val in line[0]:
                if len(val) == 5:
                    if all(elem in val for elem in digits[1]):
                        digits[3] = list(val)
                    elif all(elem in val for elem in digits[4] if elem not in digits[1]):
                        digits[5] = list(val)
                    else:
                        digits[2] = list(val)
                if len(val) == 6:
                    if not all(elem in val for elem in digits[1]):
                        digits[6] = list(val)
                    elif all(elem in val for elem in digits[4]):
                        digits[9] = list(val)
                    else:
                        digits[0] = list(val)

        invert_dict = {"".join(sorted(v)): k for k, v in digits.items()}
        concat = ""
        for d in line[1]:
            concat += str(invert_dict["".join(sorted(list(d)))])
        res += int(concat)

    return res

if __name__ == '__main__':
    start_time = time.time()

    # input_file = '2021_day_08_input_sample.txt'
    input_file = '2021_day_08_input.txt'
    input = load_input(input_file)

    """Part One"""
    result = solve_part_one(input)
    print(f'Day 8 Part One: {result}')

    """Part Two"""
    result = solve_part_two(input)
    print(f'Day 8 Part Two: {result}')

    print("--- %.2f seconds ---" % (time.time() - start_time))

