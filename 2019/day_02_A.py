# https://adventofcode.com/2019/day/2

def intcode(map):
    cur_address = 0
    while map[cur_address] != 99:
        opcode = map[cur_address]
        address_1 = map[cur_address + 1]
        address_2 = map[cur_address + 2]
        address_3 = map[cur_address + 3]
        if opcode == 1:
            # Add
            map[address_3] = map[address_1] + map[address_2]
        if opcode == 2:
            # Mul
            map[address_3] = map[address_1] * map[address_2]
        cur_address += 4
    return map[0]

map = [int(v) for v in open('2019/day_02_input.txt', 'r').read().split(',')]
map[1] = 12 # noun
map[2] = 2  # verb

# map = [int(v) for v in "1,1,1,4,99,5,6,0,99".split(",")]


print(intcode(map))