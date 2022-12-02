# -*- coding: utf-8 -*-
""" https://adventofcode.com/2022/day/1 """

from aoc_performance import aoc_perf

ROCK = 1
PAPER = 2
CISORS = 3


def score_outcome(opponent: int, you: int) -> int:
    if opponent == you:
        return 3
    if (
        (opponent == ROCK and you == CISORS)
        or (opponent == PAPER and you == ROCK)
        or (opponent == CISORS and you == PAPER)
    ):
        return 0
    return 6


def part_A(filename: str) -> int:
    total_score = 0
    hands = {"A": ROCK, "B": PAPER, "C": CISORS, "X": ROCK, "Y": PAPER, "Z": CISORS}
    with open(filename, "r") as f:
        while content := f.readline():
            opponent, you = map(lambda x: hands[x], content.strip().split(" "))
            total_score += you + score_outcome(opponent, you)
    return total_score


def outcome_to_score(outcome):
    outcome_dict = {}
    lines = outcome.split("\n")
    header = lines[1]
    for line in lines[2:-1]:
        for i in range(1, 4):
            outcome_dict[line[0] + " " + header[i]] = int(line[i])
    return outcome_dict


def part_A2(filename: str) -> int:
    """You play
    X: Rock
    Y: Paper
    Z: Cisors
    """
    outcome_txt = """
 XYZ
A360
B036
C603
"""
    outcome = outcome_to_score(outcome_txt)

    total_score = 0
    hand_score = {"X": 1, "Y": 2, "Z": 3}
    with open(filename, "r") as f:
        while content := f.readline():
            hand = content.strip().split(" ")[-1]
            total_score += hand_score[hand] + outcome[content.strip()]
    return total_score


def part_B(filename: str) -> int:
    """You
    X: Loose hand
    Y: Draw hand
    Z: Win hand
    """
    hand_score_txt = """
 XYZ
A312
B123
C231
"""
    hand_score = outcome_to_score(hand_score_txt)

    total_score = 0
    outcome_score = {"X": 0, "Y": 3, "Z": 6}
    with open(filename, "r") as f:
        while content := f.readline():
            hand = content.strip().split(" ")[-1]
            total_score += outcome_score[hand] + hand_score[content.strip()]
    return total_score


def main():
    # input_filename = "2022_day_02_input_sample.txt"
    input_filename = "2022_day_02_input.txt"

    with aoc_perf():
        print("Day 02 Part A")
        answer = part_A(input_filename)
        print(f"Answer: {answer}")

    with aoc_perf():
        print("Day 02 Part A - alternative")
        answer = part_A2(input_filename)
        print(f"Answer: {answer}")

    with aoc_perf():
        print("Day 02 Part B")
        answer = part_B(input_filename)
        print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
