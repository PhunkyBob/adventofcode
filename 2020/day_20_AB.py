# https://adventofcode.com/2020/day/20

import re 
import numpy as np
import time
from operator import mul
from functools import reduce 

# input_file = "day_20_input_sample.txt"
input_file = "day_20_input.txt"

class Tile:
    id: int = 0
    top: str = ""
    bottom: str = ""
    left: str = ""
    right: str = ""
    content: str = ""

    top_adj: int = 0
    bottom_adj: int = 0
    left_adj: int = 0
    right_adj: int = 0

    def __init__(self, input: str):
        lines = input.split("\n")
        self.id = int(re.match("Tile (\d+):", lines[0]).groups()[0])
        self.content = "\n".join([l for l in lines[1:]])
        self.__update_borders()

    def __update_borders(self):
        lines = self.content.split("\n")
        self.top = lines[0]
        self.bottom = lines[-1]
        self.left = "".join([l[0] for l in lines])
        self.right = "".join([l[-1] for l in lines])

    def get_trimmed(self):
        return "\n".join([l[1:-1] for l in self.content.split("\n")[1:-1]])

    def get_trimmed_as_array(self):
        return [list(l[1:-1]) for l in self.content.split("\n")[1:-1]]

    def is_rotable(self):
        return self.top_adj == self.bottom_adj == self.left_adj == self.right_adj == 0

    def rotate(self):
        if self.is_rotable():
            # self.top, self.left, self.bottom, self.right = self.left[::-1], self.bottom, self.right[::-1], self.top
            new_content = []
            for c in range(len(self.content.split("\n")[0])):
                new_row = ''.join(row[c] for row in self.content.split("\n"))[::-1]
                new_content.append(new_row)
            self.content = "\n".join(new_content)
            self.__update_borders()


    # def flip_h(self):
    #     if self.is_rotable():
    #         self.top, self.left, self.bottom, self.right = self.top[::-1], self.right, self.bottom[::-1], self.left

    def flip(self):
        if self.is_rotable():
            # self.top, self.left, self.bottom, self.right = self.bottom, self.left[::-1], self.top, self.right[::-1]
            self.content = "\n".join(reversed(self.content.split("\n")))
            self.__update_borders()

    def all_positions(self):
        yield 
        for action in ('r', 'r', 'r', 'f', 'r', 'r', 'r'):
            if self.is_rotable():
                if action == 'r':
                    self.rotate()
                if action == 'f':
                    self.flip()
                yield
            else:
                break

        return



class AllTiles:
    tiles: dict = {}
    merged: list = []

    def __init__(self, tiles):
        self.tiles = {t.id: t for t in tiles}

    def get_corners(self):
        corners = []
        for _, t in self.tiles.items():
            if sum([t.top_adj == 0, t.left_adj == 0, t.bottom_adj == 0, t.right_adj == 0]) == 2:
                print(f"{t.id} is a corner")
                corners.append(t.id)
        return corners

    def find_tile_with_border(self, border: str = ""):
        return sum(1 for _, t in self.tiles.items() if border in (t.left, t.right, t.top, t.bottom))

    # Check if there is some multiple combinations.
    def check_unicity(self):
        for t_id, t in self.tiles.items():
            for border in (t.left, t.right, t.top, t.bottom):
                if self.find_tile_with_border(border) > 2:
                    print(f"Duplicate candidates with tile {t_id}")

    def sort_tiles(self):
        _, first_tile = next(iter(self.tiles.items()))
        self.__find_adj(first_tile)


    def __find_adj(self, tile):
        for _, t in self.tiles.items():
            if t.id != tile.id:
                for _ in t.all_positions():
                    if tile.right_adj == 0:
                        if tile.right == t.left:
                            tile.right_adj = t.id
                            t.left_adj = tile.id
                            self.__find_adj(t)
                            break
                    if tile.bottom_adj == 0:
                        if tile.bottom == t.top:
                            tile.bottom_adj = t.id
                            t.top_adj = tile.id
                            self.__find_adj(t)
                            break
                    if tile.left_adj == 0:
                        if tile.left == t.right:
                            tile.left_adj = t.id
                            t.right_adj = tile.id
                            self.__find_adj(t)
                            break
                    if tile.top_adj == 0:
                        if tile.top == t.bottom:
                            tile.top_adj = t.id
                            t.bottom_adj = tile.id
                            self.__find_adj(t)
                            break
        return

    def __all_tiles_on_right(self, starting):
        current = self.tiles[starting]
        yield current
        while current.right_adj:
            current = self.tiles[current.right_adj]
            yield current

    def __all_tiles_on_bottom(self, starting):
        current = self.tiles[starting]
        yield current
        while current.bottom_adj:
            current = self.tiles[current.bottom_adj]
            yield current

    def __get_top_left(self):
        for id, t in self.tiles.items():
            if t.top_adj == 0 and t.left_adj == 0:
                return id

    def merge(self):
        columns = []
        for t1 in self.__all_tiles_on_right(self.__get_top_left()):
            elements = []
            for t2 in self.__all_tiles_on_bottom(t1.id):
                elements.append(t2.get_trimmed_as_array())
            columns.append(np.concatenate(elements, axis=0))
        self.merged = np.concatenate(columns, axis=1)
        # print("\n".join(["".join(l) for l in self.merged]))

    def count_pattern(self, pattern_txt):
        pattern_tile = Tile("Tile 0:\n" + pattern_txt)
        monster_count = 0

        for _ in pattern_tile.all_positions():
            # Get all "#" cooridnates in pattern.
            pattern = []
            for y, line in enumerate(pattern_tile.content.split("\n")):
                for x, char in enumerate(line):
                    if char == "#":
                        pattern.append((x, y)) 
            max_x = max(x for x, y in pattern)
            max_y = max(y for x, y in pattern)
            # Loop on all elems to find if there is a monster
            
            for y in range(len(self.merged) - max_y):
                for x in range(len(self.merged[y]) - max_x):
                    if all(self.merged[y + m_y][x + m_x] == '#' for m_x, m_y in pattern):
                        # print(f"monster found at {x}, {y}")
                        monster_count += 1
            if monster_count:
                return monster_count
        return monster_count
        

tiles = AllTiles([Tile(t) for t in open(input_file, "r").read().split("\n\n")])

tiles.check_unicity()




# Part One
start_time = time.time()
tiles.sort_tiles()
part_one = reduce(mul, tiles.get_corners(), 1)
print(f"Part One: {part_one}")
print("--- %.2f seconds ---" % (time.time() - start_time))

# Part Two


start_time = time.time()
# Merge all tiles
tiles.merge()
full_picture = "\n".join(["".join(l) for l in tiles.merged])
monster = open("day_20_monster.txt", "r").read()
monster_count = tiles.count_pattern(monster)
part_two = full_picture.count("#") - monster.count("#") * monster_count
print(f"Part Two: {part_two}")
print("--- %.2f seconds ---" % (time.time() - start_time))