# https://adventofcode.com/2020/day/14
import re

# Part One

# file = open("day_14_input_sample1.txt", "r")
file = open("day_14_input.txt", "r")

def apply_mask_1(input, mask):
    input = ("0"*len(mask) + str(bin(input)).replace("0b", ""))[-len(mask):]
    result = ""
    for i in range(len(input)):
        result += input[i] if mask[i] == 'X' else mask[i]
    return int(result, 2)


mask = ""
memory = {}
for line in file:
    match = re.match("mask = (.+)", line.strip())
    if match:
        mask = match[1]

    match = re.match(r"mem\[(\d+)\] = (\d+)", line.strip())
    if match:
        address = int(match[1])
        value = int(match[2])
        memory[address] = apply_mask_1(value, mask)

memory_sum = sum(memory[key] for key in memory)
print(f"Part One: {memory_sum}")


# Part Two

# file = open("day_14_input_sample2.txt", "r")
file = open("day_14_input.txt", "r")

def apply_mask_2(address, value, mask):
    address = ("0"*len(mask) + str(bin(address)).replace("0b", ""))[-len(mask):]
    result = ""
    for i in range(len(address)):
        result += address[i] if mask[i] == '0' else mask[i]
    
    change_bit(result, value)

def change_bit(adress, value):
    if 'X' not in adress:
        memory[int(adress, 2)] = value
    else:
        for b in ('0', '1'):
            change_bit(adress.replace('X', b, 1), value)


mask = ""
memory = {}
for line in file:
    match = re.match("mask = (.+)", line.strip())
    if match:
        mask = match[1]

    match = re.match(r"mem\[(\d+)\] = (\d+)", line.strip())
    if match:
        index = int(match[1])
        value = int(match[2])
        apply_mask_2(index, value, mask)

memory_sum = sum(memory[key] for key in memory)
print(f"Part Two: {memory_sum}")

    
