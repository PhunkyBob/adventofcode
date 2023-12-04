"""
Advent of Code 2023
--- Day 4: Scratchcards ---
https://adventofcode.com/2023/day/4

For example:

Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11

In the above example, card 1 has five winning numbers (41, 48, 83, 86, and 17) and eight numbers you have (83, 86, 6, 31, 17, 9, 48, and 53). Of the numbers you have, four of them (48, 83, 17, and 86) are winning numbers! That means card 1 is worth 8 points (1 for the first match, then doubled three times for each of the three matches after the first).

    Card 2 has two winning numbers (32 and 61), so it is worth 2 points.
    Card 3 has two winning numbers (1 and 21), so it is worth 2 points.
    Card 4 has one winning number (84), so it is worth 1 point.
    Card 5 has no winning numbers, so it is worth no points.
    Card 6 has no winning numbers, so it is worth no points.

So, in this example, the Elf's pile of scratchcards is worth 13 points.
"""

from typing import List
from aoc_performance import aoc_perf
import re

DAY = "04"


def get_score(nb_common: int) -> int:
    return nb_common if nb_common < 2 else 1 * (2 ** (nb_common - 1))


def get_line_score(line: str) -> int:
    if elems := re.match(r"(.+):(.+)\|(.+)", line):
        winning_numbers = set(map(int, filter(None, elems[2].strip().split(" "))))
        played_numbers = set(map(int, filter(None, elems[3].strip().split(" "))))
        return get_score(len(winning_numbers.intersection(played_numbers)))
    return 0


def read_input(input_filename: str) -> List[int]:
    with open(input_filename) as f:
        return [get_line_score(line) for line in f]


def part_A(input_filename: str) -> int:
    scores = read_input(input_filename)
    return sum(scores)


def part_B(input_filename: str) -> int:
    result: List[int] = []
    next_cards_must_copy = [0]
    with open(input_filename) as f:
        for line in f:
            if elems := re.match(r"(.+):(.+)\|(.+)", line):
                winning_numbers = set(map(int, filter(None, elems[2].strip().split(" "))))
                played_numbers = set(map(int, filter(None, elems[3].strip().split(" "))))
                this_card_occurence = next_cards_must_copy.pop(0) + 1 if next_cards_must_copy else 1
                for i in range(len(winning_numbers.intersection(played_numbers))):
                    if i < len(next_cards_must_copy):
                        next_cards_must_copy[i] += this_card_occurence
                    else:
                        next_cards_must_copy.append(this_card_occurence)
                result.append(this_card_occurence)
    return sum(result)


def main() -> None:
    input_filename = f"day_{DAY}_input.txt"
    # input_filename = f"day_{DAY}_input_sample.txt"

    with aoc_perf(memory=True):
        print(f"Day {DAY} Part A")
        answer = part_A(input_filename)
        print(f"Answer: {answer}")

    with aoc_perf(memory=True):
        print(f"Day {DAY} Part B")
        answer = part_B(input_filename)
        print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
