# https://adventofcode.com/2020/day/11

import copy

# seats = [[c for c in x.strip()] for x in open("day_11_input_sample.txt", "r")]
seats = [[c for c in x.strip()] for x in open("day_11_input.txt", "r")]


def seats_str(seats):
    str = ''
    for line in seats:
        str += "".join(line) + '\n'
    return str

def count_occupied_around(seats, v, h):
    v_from = max(v - 1, 0)
    v_to = min(v + 2, len(seats))
    h_from = max(h - 1, 0)
    h_to = min(h + 2, len(seats[0]))

    count = 0
    for cur_v in range(v_from, v_to):
        for cur_h in range(h_from, h_to):
            if not (cur_h == h and cur_v == v) and seats[cur_v][cur_h] == '#':
                count += 1
    return(count)


def next_round(seats):
    new_seats = copy.deepcopy(seats)
    for v in range(len(seats)):
        for h in range(len(seats[0])):
            if seats[v][h] == 'L' and count_occupied_around(seats, v, h) == 0:
                new_seats[v][h] = '#'
            if seats[v][h] == '#' and count_occupied_around(seats, v, h) >= 4:
                new_seats[v][h] = 'L'
    return new_seats


# print(seats_str(seats))
new_seats = next_round(seats)
while new_seats != seats:
    # print(seats_str(new_seats))
    seats = copy.deepcopy(new_seats)
    new_seats = next_round(seats)

# print("Part One: Last state")
# print(seats_str(new_seats))

occupied = 0
for line in seats:
    occupied += sum(1 for s in line if s == '#')
print(f"Part One, total occupied seats: {occupied}")