# https://adventofcode.com/2020/day/20

import re 


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

    def __init__(self, input):
        lines = input.split("\n")
        self.id = int(re.match("Tile (\d+):", lines[0]).groups()[0])
        self.top = lines[1]
        self.bottom = lines[-1]
        self.left = "".join([l[0] for l in lines[1:]])
        self.right = "".join([l[-1] for l in lines[1:]])
        self.content = lines[1:]

    def is_rotable(self):
        return self.top_adj == self.bottom_adj == self.left_adj == self.right_adj == 0

    def rotate(self):
        if self.is_rotable():
            self.top, self.left, self.bottom, self.right = self.left[::-1], self.bottom, self.right[::-1], self.top

    def flip_h(self):
        if self.is_rotable():
            self.top, self.left, self.bottom, self.right = self.top[::-1], self.right, self.bottom[::-1], self.left

    def flip_v(self):
        if self.is_rotable():
            self.top, self.left, self.bottom, self.right = self.bottom, self.left[::-1], self.top, self.right[::-1]

    def find_adj(self):
        for t in tiles:
            if t.id != self.id:
                for action in ('r', 'r', 'r', 'r', 'f', 'r', 'r', 'r', 'r'):
                    if self.right_adj == 0:
                        if self.right == t.left:
                            self.right_adj = t.id
                            t.left_adj = self.id
                            t.find_adj()
                            break
                    if self.bottom_adj == 0:
                        if self.bottom == t.top:
                            self.bottom_adj = t.id
                            t.top_adj = self.id
                            t.find_adj()
                            break
                    if self.left_adj == 0:
                        if self.left == t.right:
                            self.left_adj = t.id
                            t.right_adj = self.id
                            t.find_adj()
                            break
                    if self.top_adj == 0:
                        if self.top == t.bottom:
                            self.top_adj = t.id
                            t.bottom_adj = self.id
                            t.find_adj()
                            break
                    if self.right_adj == 0 or self.bottom_adj == 0:
                        if t.is_rotable():
                            if action == 'r':
                                t.rotate()
                            if action == 'f':
                                t.flip_h()
                        else:
                            break
        return


def find_tile(border: str = ""):
    return sum(1 for t in tiles if border in (t.left, t.right, t.top, t.bottom))

# tiles = [Tile(t) for t in open("day_20_input_sample.txt", "r").read().split("\n\n")]
tiles = [Tile(t) for t in open("day_20_input.txt", "r").read().split("\n\n")]

# Check if there is some multiple combinations.
for t in tiles:
    for border in (t.left, t.right, t.top, t.bottom):
        if find_tile(border) > 2:
            print(f"Duplicate candidates with tile {t.id}")

# for t in tiles:
    # t.find_adj()
tiles[0].find_adj()

part_one = 1
for t in tiles:
    if sum([t.top_adj == 0, t.left_adj == 0, t.bottom_adj == 0, t.right_adj == 0]) == 2:
        print(f"{t.id} is a corner")
        part_one *= t.id
print(f"Part One: {part_one}")