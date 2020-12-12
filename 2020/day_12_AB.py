# https://adventofcode.com/2020/day/12

from collections import namedtuple

Instruction = namedtuple("Instruction", ['action', 'value'])

input_sample = """F10
N3
F7
R90
F11"""
# input = [Instruction(x[0], int(x[1:]))  for x in input_sample.split()]
input = [Instruction(x[0], int(x[1:]))  for x in open("day_12_input.txt", "r")]

directions = {
    'N': (0, 1),
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0)
}

# Part One
pos_x = 0
pos_y = 0
facings = ['E', 'S', 'W', 'N']
facing_index = 0
facing = facings[(facing_index // 90) % 4]
for i in input:
    if i.action == 'F':
        pos_x += directions[facing][0] * i.value
        pos_y += directions[facing][1] * i.value
    if i.action in ('N', 'E', 'S', 'W'):
        pos_x += directions[i.action][0] * i.value
        pos_y += directions[i.action][1] * i.value
    if i.action == 'R':
        facing_index += i.value
        facing = facings[int((facing_index / 90) % 4)]
    if i.action == 'L':
        facing_index -= i.value
        facing = facings[int((facing_index / 90) % 4)]
print(f"Part One, ends in [{pos_x}, {pos_y}]")
print(f"Manhattan distance: {abs(pos_x) + abs(pos_y)}")


# Part Two
pos_x = 0
pos_y = 0
waypoint_x = 10
waypoint_y = 1

for i in input:
    if i.action == 'F':
        pos_x += waypoint_x * i.value
        pos_y += waypoint_y * i.value
    if i.action in ('N', 'E', 'S', 'W'):
        waypoint_x += directions[i.action][0] * i.value
        waypoint_y += directions[i.action][1] * i.value
    if i.action == 'R':
        for turn in range(i.value // 90):
            waypoint_x, waypoint_y = waypoint_y, 0 - waypoint_x
    if i.action == 'L':
        for turn in range(i.value // 90):
            waypoint_x, waypoint_y = 0 - waypoint_y, waypoint_x
print(f"Part Two, ends in [{pos_x}, {pos_y}]")
print(f"Manhattan distance: {abs(pos_x) + abs(pos_y)}")
