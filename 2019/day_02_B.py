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

clean_map = [int(v) for v in open('2019/day_02_input.txt', 'r').read().split(',')]

for i in range(0, 99):
    for j in range(0, 99):
        map = clean_map.copy()
        map[1] = i # noun
        map[2] = j  # verb
        if intcode(map) == 19690720:
            print(f"{i:02d}{j:02d}")
            break
