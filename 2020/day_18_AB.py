# https://adventofcode.com/2020/day/18

from pyparsing import *
import time

# inputs = open("day_18_input_sample.txt", "r").read().split("\n")
inputs = open("day_18_input.txt", "r").read().split("\n")


def evaluate(input_list):
    if type(input_list) is str or type(input_list) is int:
        return int(input_list)

    operator = "+"
    result = 0
    for e in input_list:
        if e in ('*', '+'):
            operator = e
        else:
            if operator == '+':
                result += evaluate(e)
            if operator == '*':
                result *= evaluate(e)

    return result


# Part One
start_time = time.time()
total = 0
for elem in inputs:
    input_list = nestedExpr('(',')').parseString("(" + elem + ")").asList()
    # print(f"{elem} becomes {evaluate(input_list)}")
    total += evaluate(input_list)

print(f"Part One: {total}")
print("--- %.2f seconds ---" % (time.time() - start_time))

            
# Part Two
start_time = time.time()
my_precedence = infixNotation(pyparsing_common.integer,
    [
    (oneOf('+ -'), 2, opAssoc.LEFT),
    (oneOf('* /'), 2, opAssoc.LEFT),
    ])

total = 0
for elem in inputs:
    input_list = my_precedence.parseString("(" + elem + ")").asList()
    # print(f"{elem} becomes {evaluate(input_list)}")
    total += evaluate(input_list)

print(f"Part Two: {total}")
print("--- %.2f seconds ---" % (time.time() - start_time))