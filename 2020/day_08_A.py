# https://adventofcode.com/2020/day/8
import re

# instructions = open('day_08_input_sample.txt', 'r').read().split("\n")
instructions = open('day_08_input.txt', 'r').read().split("\n")


actions = {
    'nop': lambda v: (1, 0),
    'acc': lambda v: (1, int(v)),
    'jmp': lambda v: (int(v), 0),
}

# Part One
lines_used = [0 for i in range(len(instructions))]

accumulator = 0
current_line = 0
while lines_used[current_line] == 0:
    lines_used[current_line] += 1
    operation, value = re.match(r'(\w+) ([\+\-\d]+)', instructions[current_line]).groups()
    add_line, add_acc = actions[operation](value)
    current_line += add_line
    accumulator += add_acc
    
print(accumulator)