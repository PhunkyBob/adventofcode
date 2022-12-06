# -*- coding: utf-8 -*-
""" 
--- Day 1: Calorie Counting ---
https://adventofcode.com/2022/day/1 

Tthe Elves begin taking inventory of their supplies. One important 
consideration is food - in particular, the number of Calories each 
Elf is carrying (your puzzle input).

1000
2000
3000

4000

5000
6000

7000
8000
9000

10000

This list represents the Calories of the food carried by five Elves:
- The first Elf is carrying food with 1000, 2000, and 3000 Calories, a 
total of 6000 Calories.
- The second Elf is carrying one food item with 4000 Calories.
- The third Elf is carrying food with 5000 and 6000 Calories, a total 
of 11000 Calories.
- The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a 
total of 24000 Calories.
- The fifth Elf is carrying one food item with 10000 Calories.
"""

from aoc_performance import aoc_perf
from typing import List


def get_bag(filename: str) -> dict:
    """This function cumulate the value of each bag on the fly.
    Pros: File is not loaded in memory all at once.
    """
    bag = {}
    with open(filename, "r") as f:
        elf_no = 0
        bag[elf_no] = 0
        while content := f.readline():
            content = content.strip()
            if not content:
                elf_no += 1
                bag[elf_no] = 0
                continue
            bag[elf_no] += int(content)
    return bag


def part_A(filename: str) -> int:
    bag = get_bag(filename)
    return max(bag.values())


def part_B(filename: str, top_n: int = 3) -> int:
    bag = get_bag(filename)
    sorted_bags = sorted(bag.values(), reverse=True)
    return sum(sorted_bags[:3])


def part_B2(filename: str) -> int:
    """This version uses generators for less memory usage."""
    with open(filename, "r") as f:
        gen_bags = (bags.strip() for bags in f.read().split("\n\n"))

    def sum_bag(bag: str) -> int:
        return sum(map(int, bag.split("\n")))

    sorted_bags = sorted(map(sum_bag, gen_bags), reverse=True)
    return sum(sorted_bags[:3])


def part_B3(filename: str) -> int:
    """This version don't store the list, only the best N."""
    top_n = TopN(3)
    with open(filename, "r") as f:
        elf_bag_value = 0
        while content := f.readline():
            content = content.strip()
            if not content:
                top_n.update(elf_bag_value)
                elf_bag_value = 0
                continue
            elf_bag_value += int(content)

    return sum(top_n.shortlist)


class TopN:
    shortlist: List[int]
    min_val_of_shortlist: int

    def __init__(self, size: int = 1) -> None:
        self.shortlist = [0] * size
        self.min_val_of_shortlist = 0

    def update(self, value: int) -> None:
        if value > self.min_val_of_shortlist:
            self.shortlist.append(value)
            self.shortlist.sort()
            self.shortlist.pop(0)
            self.min_val_of_shortlist = min(self.shortlist)


def main():
    # input_filename = "2022_day_01_input_sample.txt"
    input_filename = "2022_day_01_input.txt"

    with aoc_perf():
        print("Day 01 Part A")
        answer = part_A(input_filename)
        print(f"Answer: {answer}")

    with aoc_perf(memory=True):
        print("Day 01 Part B")
        answer = part_B(input_filename)
        print(f"Answer: {answer}")

    with aoc_perf(memory=True):
        print("Day 01 Part B - alternative")
        answer = part_B2(input_filename)
        print(f"Answer: {answer}")

    with aoc_perf(memory=True):
        print("Day 01 Part B - alternative 2")
        answer = part_B3(input_filename)
        print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
