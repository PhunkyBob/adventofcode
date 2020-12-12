# https://adventofcode.com/2020/day/11

import copy
import re 
import time


# seats_input = open("day_11_input_sample.txt", "r").read().replace("\n", "")
# WIDTH = len(open("day_11_input_sample.txt", "r").readline().strip())
seats_input = open("day_11_input.txt", "r").read().replace("\n", "")
WIDTH = len(open("day_11_input.txt", "r").readline().strip())

"""
Display seats, for debug purpose.
"""
def seats_str(seats):
    return re.sub("(.{" + str(WIDTH) + "})", r"\1\n", seats)


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
                (0 <= v + dir_v * dist < len(seats) // WIDTH)
                and (0 <= h + dir_h * dist < WIDTH)
                and not occupied_in_this_direction
                and not free_in_this_direction
                and (dist <= max_dist or max_dist == -1)
            ):
                look_v = v + dir_v * dist
                look_h = h + dir_h * dist
                if seats[look_v * WIDTH + look_h] == "#":
                    occupied_in_this_direction = True
                if seats[look_v * WIDTH + look_h] == "L":
                    free_in_this_direction = True
                dist += 1
            if occupied_in_this_direction:
                total_occupied += 1

    return total_occupied

def change_pos(input, pos, value):
    return input[:pos] + value + input[pos+1:]
    # text = list(input)
    # text[pos] = value
    # return ''.join(text)

# Part One
def next_round_part1(seats):
    new_seats = seats
    for v in range(len(seats) // WIDTH):
        for h in range(WIDTH):
            if seats[v * WIDTH + h] == "L" and count_occupied_directions(seats, v, h, 1) == 0:
                new_seats = change_pos(new_seats, v * WIDTH + h, "#")
            if seats[v * WIDTH + h] == "#" and count_occupied_directions(seats, v, h, 1) >= 4:
                new_seats = change_pos(new_seats, v * WIDTH + h, "L")
    return new_seats

start_time = time.time()

# print(seats_str(seats_input))
seats = seats_input
new_seats = next_round_part1(seats)
while new_seats != seats:
    # print(seats_str(new_seats))
    seats = new_seats
    new_seats = next_round_part1(seats)

# print("Part One: Last state")
# print(seats_str(new_seats))

occupied = seats.count("#")
print(f"Part One, total occupied seats: {occupied}")
print("--- %.2f seconds ---" % (time.time() - start_time))


# Part Two
def next_round_part2(seats):
    new_seats = seats
    for v in range(len(seats) // WIDTH):
        for h in range(WIDTH):
            if seats[v * WIDTH + h] == "L" and count_occupied_directions(seats, v, h) == 0:
                new_seats = change_pos(new_seats, v * WIDTH + h, "#")
            if seats[v * WIDTH + h] == "#" and count_occupied_directions(seats, v, h) >= 5:
                new_seats = change_pos(new_seats, v * WIDTH + h, "L")
    return new_seats

start_time = time.time()
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
print("--- %.2f seconds ---" % (time.time() - start_time))