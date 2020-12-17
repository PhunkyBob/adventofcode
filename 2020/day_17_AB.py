# https://adventofcode.com/2020/day/17

from itertools import product
import time


# input = open("day_17_input_sample.txt", "r").read()
input = open("day_17_input.txt", "r").read()

def active_neighbors(cubes, coords):
    all_ranges = (range(d - 1, d + 2) for d in coords)
    total_active = 0
    for c in product(*all_ranges):
        if c != coords:
            if c in cubes:
                total_active += 1
    return total_active


# Limits of the cubes positions.
def get_bounds(cubes):
    maxs = next(iter(cubes))
    mins = maxs
    dims = len(maxs)
    for c in cubes:
        maxs = tuple(max(c[e], maxs[e]) for e in range(dims))
        mins = tuple(min(c[e], mins[e]) for e in range(dims))
    return mins, maxs


def next_cycle(cubes, active_to_active=(2, 3), inactive_to_active=3):
    bounds_min, bounds_max = get_bounds(cubes)
    all_ranges = (range(bounds_min[i] - 1, bounds_max[i] + 2) for i in range(len(bounds_max)))
    next_cubes = set()
    for coords in product(*all_ranges):
        an = active_neighbors(cubes, coords)
        if coords in cubes:
            # Active cube
            if an in active_to_active:
                next_cubes.add(coords)
        else:
            # Inactive cube
            if an == inactive_to_active:
                next_cubes.add(coords)
    return next_cubes

def display_cubes(cubes):
    bounds_min, bounds_max = get_bounds(cubes)
    all_ranges = (range(bounds_min[i], bounds_max[i] + 1) for i in range(2, len(bounds_max)))
    for partial_coords in product(*all_ranges):
        print(f"{list(partial_coords)}")
        for y in range(bounds_min[1], bounds_max[1] + 1):
            for x in range(bounds_min[0], bounds_max[0] + 1):
                l = tuple([x, y] + list(partial_coords))
                p = '#' if tuple(l) in cubes else '.'
                print(p, end="")
            print()
        print()




# Part One
start_time = time.time()

# Contains all active cubes.
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



# Part Two
start_time = time.time()

# Contains all active cubes.
active_cubes = set()

# Initial state
for y, line in enumerate(input.split("\n")):
    for x, value in enumerate(line):
        if value == '#':
            active_cubes.add((x, y, 0, 0))      # Add another dimension

# display_cubes(active_cubes)
# Next steps
for i in range(6):
    active_cubes = next_cycle(active_cubes)
    # print(f"Step {i+1}")
    # display_cubes(active_cubes)

print(f"Part Two: {len(active_cubes)}")
print("--- %.2f seconds ---" % (time.time() - start_time))