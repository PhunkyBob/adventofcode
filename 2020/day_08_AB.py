# https://adventofcode.com/2020/day/8
import re

# instructions = open("day_08_input_sample.txt", "r").read().split("\n")
instructions = open('day_08_input.txt', 'r').read().split("\n")


actions = {
    "nop": lambda v: (1, 0),
    "acc": lambda v: (1, int(v)),
    "jmp": lambda v: (int(v), 0),
}

# Allows to test if boot is OK and returns the accumulator value.
def test_boot(instructions):
    lines_used = [0 for i in range(len(instructions))]

    accumulator = 0
    current_line = 0
    while current_line < len(lines_used) and lines_used[current_line] == 0:
        lines_used[current_line] += 1
        operation, value = re.match(
            r"(\w+) ([\+\-\d]+)", instructions[current_line]
        ).groups()
        add_line, add_acc = actions[operation](value)
        current_line += add_line
        accumulator += add_acc
    if current_line < len(lines_used):
        # Infinite loop
        return (False, accumulator)
    else:
        # Boot success
        return (True, accumulator)

# Allows to change 1 specific line of instructions.
def change_line(instructions, line):
    if instructions[line][0:3] not in ("nop", "jmp"):
        return False
    else:
        new_instructions = instructions.copy()
        if instructions[line][0:3] == "nop":
            new_instructions[line] = new_instructions[line].replace("nop", "jmp")    
        if instructions[line][0:3] == "jmp":
            new_instructions[line] = new_instructions[line].replace("jmp", "nop")    
        return new_instructions


# Part One
print("Part One")

boot_ok, accumulator = test_boot(instructions)
print(f"Boot OK: {boot_ok}")
print(f"Accumulator: {accumulator}")


# Part Two
print("\nPart Two")

boot_ok = False
accumulator = 0
line_to_change = 0
while not boot_ok and line_to_change < len(instructions):
    new_instructions = change_line(instructions, line_to_change)
    if new_instructions:
        boot_ok, accumulator = test_boot(new_instructions)
    line_to_change += 1


print(f"Changed line {line_to_change - 1}")
print(f"Boot OK: {boot_ok}")
print(f"Accumulator: {accumulator}")
