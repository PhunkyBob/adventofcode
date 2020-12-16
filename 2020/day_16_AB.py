# https://adventofcode.com/2020/day/16

import re
import itertools

# input_parts = open("day_16_input_sample1.txt", "r").read().split("\n\n")
# input_parts = open("day_16_input_sample2.txt", "r").read().split("\n\n")
input_parts = open("day_16_input.txt", "r").read().split("\n\n")

# Part One
rules = {}
all_possible_values = set()
for line in input_parts[0].split("\n"):
    name, from_1, to_1, from_2, to_2 = re.match(r"([\w\s]+): (\d+)-(\d+) or (\d+)-(\d+)", line).groups()
    #possible_values = set([i for range(from_1, to_1)]).union(set([i for range(from_2, to_2)]))
    possible_values = {i for i in range(int(from_1), int(to_1) + 1)}.union({i for i in range(int(from_2), int(to_2) + 1)})
    rules[name] = possible_values
    all_possible_values = all_possible_values.union(possible_values)

all_invalid_values = []
all_valid_lines = []
for line in input_parts[2].split("\n")[1:]:
    invalid_values = [int(v) for v in line.split(',') if int(v) not in all_possible_values]
    if len(invalid_values) > 0:
        all_invalid_values += invalid_values
    else:
        all_valid_lines.append(line)
error_rate = sum(all_invalid_values)
print(f"Part One: {error_rate}")


# Part Two
tickets = {}
correspondance = {}
# My ticket
for i, v in enumerate(input_parts[1].split("\n")[1].split(',')):
    tickets[f'col_{i}'] = [int(v)]
    # tickets[f'col_{i}'] = []
    correspondance[f'col_{i}'] = []

# Others tickets
for line in all_valid_lines:
    for i, v in enumerate(line.split(',')):
        tickets[f'col_{i}'].append(int(v))

# Check all cols
for key in tickets:
    possible_fields = []
    for r in rules:
        if len(set(tickets[key]) - rules[r]) == 0:
            possible_fields.append(r)
    correspondance[key] = possible_fields

def remove(elem):
    actions = 0
    for key in correspondance:
        if len(correspondance[key]) > 1 and elem in correspondance[key]:
            correspondance[key].remove(elem)
            actions += 1
    return actions

actions = 1
while actions > 0:
    actions = 0
    for key in correspondance:
        if len(correspondance[key]) == 1:
            # Lui il est tout seul
            actions += remove(correspondance[key][0])
    
print(correspondance)

# My ticket
answer = 1
for i, v in enumerate(input_parts[1].split("\n")[1].split(',')):
    if "departure" in correspondance[f'col_{i}'][0]:
        answer *= int(v)
print(f"Part Two: {answer}")