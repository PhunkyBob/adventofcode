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

actions = {
    "e": lambda x, y: (x, y + 2),
    "se": lambda x, y: (x + 1, y + 1),
    "sw": lambda x, y: (x + 1, y - 1),
    "w": lambda x, y: (x, y - 2),
    "nw": lambda x, y: (x - 1, y - 1),
    "ne": lambda x, y: (x - 1, y + 1),
}

# Part One
start_time = time.time()
final_tiles = {} # List of all final tiles. True = black

for line in lines:
    pos_x = pos_y = 0
    for instruction in re.findall("(e|se|sw|w|nw|ne)", line):
        pos_x, pos_y = actions[instruction](pos_x, pos_y)
    if (pos_x, pos_y) in final_tiles:
        final_tiles[(pos_x, pos_y)] = not final_tiles[(pos_x, pos_y)]
    else:
        final_tiles[(pos_x, pos_y)] = True

answer = sum(1 for t in final_tiles if final_tiles[t] == True)
print(f"Part One: {answer}")
print("--- %.2f seconds ---" % (time.time() - start_time))

# Part Two
start_time = time.time()

def count_adjacent_black(tile, all_tiles):
    count = 0
    for a in actions:
        search_t = actions[a](tile[0], tile[1])
        if search_t in all_tiles and all_tiles[search_t]:
            count += 1
    return count

for r in range(100):
    # Add all tiles adjacent to a black tile.
    new_tiles = copy.deepcopy(final_tiles)
    for t in final_tiles:
        if final_tiles[t] == True:
            for a in actions:
                new_t = actions[a](t[0], t[1])
                if new_t not in final_tiles:
                    new_tiles[new_t] = False
    # Flip all requireded tiles.
    for t in new_tiles:
        adj_black = count_adjacent_black(t, final_tiles)
        if new_tiles[t] == True:
            # Black
            if adj_black == 0 or adj_black > 2:
                new_tiles[t] = False
        else:
            # White
            if adj_black == 2:
                new_tiles[t] = True
    final_tiles = new_tiles
    # answer = sum(1 for t in final_tiles if final_tiles[t] == True)
    # print(f"Part Two after {r+1} rounds: {answer}")

answer = sum(1 for t in final_tiles if final_tiles[t] == True)
print(f"Part Two: {answer}")
print("--- %.2f seconds ---" % (time.time() - start_time))