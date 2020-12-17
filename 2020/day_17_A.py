# https://adventofcode.com/2020/day/17

from itertools import product
import time


# input = open("day_17_input_sample.txt", "r").read()
input = open("day_17_input.txt", "r").read()

def active_neighbors(cubes, x, y, z):
    total_active = 0
    for search_x, search_y, search_z in product(range(x - 1 , x + 2), range(y - 1 , y + 2), range(z - 1 , z + 2)):
        if search_x != x or search_y != y or search_z != z:
            if (search_x, search_y, search_z) in cubes:
                total_active += 1
    return total_active


# Limits of the cubes positions.
def get_bounds(cubes):
    max_x, max_y, max_z = next(iter(cubes))
    min_x, min_y, min_z = max_x, max_y, max_z
    for x, y, z in cubes:
        min_x = min(x, min_x)
        max_x = max(x, max_x)
        min_y = min(y, min_y)
        max_y = max(y, max_y)
        min_z = min(z, min_z)
        max_z = max(z, max_z)
    return min_x, max_x, min_y, max_y, min_z, max_z


def next_cycle(cubes):
    min_x, max_x, min_y, max_y, min_z, max_z = get_bounds(cubes)
    next_cubes = set()
    for x, y, z in product(range(min_x - 1 , max_x + 2), range(min_y - 1 , max_y + 2), range(min_z - 1 , max_z + 2)):
        an = active_neighbors(cubes, x, y, z)
        if (x, y, z) in cubes:
            # Active cube
            if an in (2, 3):
                next_cubes.add((x, y, z))
        else:
            # Inactive cube
            if an == 3:
                next_cubes.add((x, y, z))
    return next_cubes

def display_cubes(cubes):
    min_x, max_x, min_y, max_y, min_z, max_z = get_bounds(cubes)
    for z in range(min_z, max_z + 1):
        print(f"Z={z}")
        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                p = '#' if (x, y, z) in cubes else '.'
                print(p, end="")
            print()
        print()



# Part One
start_time = time.time()

# Contains all alive cubes.
active_cubes = set()

# Initial state
for y, line in enumerate(input.split("\n")):
    for x, value in enumerate(line):
        if value == '#':
            active_cubes.add((x, y, 0))


# display_cubes(active_cubes)
# Next steps
for i in range(6):
    active_cubes = next_cycle(active_cubes)
    # print(f"Step {i+1}")
    # display_cubes(active_cubes)

print(f"Part One: {len(active_cubes)}")
print("--- %.2f seconds ---" % (time.time() - start_time))