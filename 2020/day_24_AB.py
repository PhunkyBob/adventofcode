# https://adventofcode.com/2020/day/24

"""
  __    __    __    __
 /  \__/  \__/  \__/  \__ 
 \__/  \__/ E\__/  \__/   
 /  \__/NE\__/SE\__/  \__ 
 \__/  \__/ X\__/  \__/   
 /  \__/NW\__/SW\__/  \__ 
 \__/  \__/ W\__/  \__/   
 /  \__/  \__/  \__/  \__ 
 \__/  \__/  \__/  \__/   
E = 	(+0, +2)
SE = 	(+1, +1)
SW = 	(+1, -1)
W = 	(+0, -2)
NW = 	(-1, -1)
NE = 	(-1, +1)
"""
import re
import copy
import time

# input_file = "day_24_input_sample.txt"
input_file = "day_24_input.txt"

lines = list(map(lambda s: s.strip(), open(input_file, "r").readlines()))

directions = {
    "e": lambda x, y: (x, y + 2),
    "se": lambda x, y: (x + 1, y + 1),
    "sw": lambda x, y: (x + 1, y - 1),
    "w": lambda x, y: (x, y - 2),
    "nw": lambda x, y: (x - 1, y - 1),
    "ne": lambda x, y: (x - 1, y + 1),
}

# Part One
start_time = time.time()
black_tiles = set() # List of all final tiles. True = black

for line in lines:
    pos_x = pos_y = 0
    for instruction in re.findall("(e|se|sw|w|nw|ne)", line):
        pos_x, pos_y = directions[instruction](pos_x, pos_y)
    if (pos_x, pos_y) in black_tiles:
        black_tiles.remove((pos_x, pos_y))
    else:
        black_tiles.add((pos_x, pos_y))

answer = len(black_tiles)
print(f"Part One: {answer}")
print("--- %.2f seconds ---" % (time.time() - start_time))

# Part Two
start_time = time.time()

def count_adjacent_black(tile, all_black_tiles):
    count = 0
    for d in directions:
        search_t = directions[d](tile[0], tile[1])
        if search_t in all_black_tiles:
            count += 1
    return count

for r in range(100):
    # Add all tiles adjacent to a black tile.
    new_black_tiles = set()
    for t in black_tiles:
        # Current black tile.
        adj_black = count_adjacent_black(t, black_tiles)
        if 0 < adj_black <= 2:
            new_black_tiles.add(t)
        
        # All white tiles around this black tile.
        for d in directions:
            new_t = directions[d](t[0], t[1])
            if new_t not in black_tiles:
                adj_black = count_adjacent_black(new_t, black_tiles)
                if adj_black == 2:
                    new_black_tiles.add(new_t)
    black_tiles = new_black_tiles
    # answer = len(black_tiles)
    # print(f"Part Two after {r+1} rounds: {answer}")

answer = len(black_tiles)
print(f"Part Two: {answer}")
print("--- %.2f seconds ---" % (time.time() - start_time))