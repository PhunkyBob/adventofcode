# https://adventofcode.com/2020/day/11

import copy

# seats_input = [[c for c in x.strip()] for x in open("day_11_input_sample.txt", "r")]
seats_input = [[c for c in x.strip()] for x in open("day_11_input.txt", "r")]

"""
Display seats, for debug purpose.
"""
def seats_str(seats):
    str = ""
    for line in seats:
        str += "".join(line) + "\n"
    return str


"""
For a matrix of seats, count occupied seats visible from position [v][h] within a max_dist.
"""
def count_occupied_directions(seats, v, h, max_dist=-1):
    total_occupied = 0
    for dir_h in (-1, 0, 1):
        for dir_v in (-1, 0, 1):
            if dir_h == 0 and dir_v == 0:
                continue
            dist = 1
            occupied_in_this_direction = False
            free_in_this_direction = False
            while (
                (0 <= v + dir_v * dist < len(seats))
                and (0 <= h + dir_h * dist < len(seats[0]))
                and not occupied_in_this_direction
                and not free_in_this_direction
                and (dist <= max_dist or max_dist == -1)
            ):
                if seats[v + dir_v * dist][h + dir_h * dist] == "#":
                    occupied_in_this_direction = True
                if seats[v + dir_v * dist][h + dir_h * dist] == "L":
                    free_in_this_direction = True
                dist += 1
            if occupied_in_this_direction:
                total_occupied += 1

    return total_occupied


# Part One
def next_round_part1(seats):
    new_seats = copy.deepcopy(seats)
    for v in range(len(seats)):
        for h in range(len(seats[0])):
            if seats[v][h] == "L" and count_occupied_directions(seats, v, h, 1) == 0:
                new_seats[v][h] = "#"
            if seats[v][h] == "#" and count_occupied_directions(seats, v, h, 1) >= 4:
                new_seats[v][h] = "L"
    return new_seats

# print(seats_str(seats))
seats = copy.deepcopy(seats_input)
new_seats = next_round_part1(seats)
while new_seats != seats:
    # print(seats_str(new_seats))
    seats = copy.deepcopy(new_seats)
    new_seats = next_round_part1(seats)

# print("Part One: Last state")
# print(seats_str(new_seats))

occupied = 0
for line in seats:
    occupied += sum(1 for s in line if s == "#")
print(f"Part One, total occupied seats: {occupied}")


# Part Two
def next_round_part2(seats):
    new_seats = copy.deepcopy(seats)
    for v in range(len(seats)):
        for h in range(len(seats[0])):
            if seats[v][h] == "L" and count_occupied_directions(seats, v, h) == 0:
                new_seats[v][h] = "#"
            if seats[v][h] == "#" and count_occupied_directions(seats, v, h) >= 5:
                new_seats[v][h] = "L"
    return new_seats

seats = copy.deepcopy(seats_input)
# print(seats_str(seats))
new_seats = next_round_part2(seats)
while new_seats != seats:
    # print(seats_str(new_seats))
    seats = copy.deepcopy(new_seats)
    new_seats = next_round_part2(seats)

# print("Part Two: Last state")
# print(seats_str(new_seats))

occupied = 0
for line in seats:
    occupied += sum(1 for s in line if s == "#")
print(f"Part Two, total occupied seats: {occupied}")