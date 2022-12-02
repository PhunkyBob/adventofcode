# -*- coding: utf-8 -*-
""" https://adventofcode.com/2022/day/1 """

from aoc_performance import aoc_perf


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


def main():
    # input_filename = "2022_day_01_input_sample.txt"
    input_filename = "2022_day_01_input.txt"

    with aoc_perf():
        print("Day 01 Part A")
        answer = part_A(input_filename)
        print(f"Answer: {answer}")

    with aoc_perf():
        print("Day 01 Part B")
        answer = part_B(input_filename)
        print(f"Answer: {answer}")

    with aoc_perf():
        print("Day 01 Part B - alternative")
        answer = part_B2(input_filename)
        print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
