# -*- coding: utf-8 -*-
""" 
--- Day 2: Rock Paper Scissors ---
https://adventofcode.com/2022/day/2 

Rock Paper Scissors is a game between two players. 
Appreciative of your help yesterday, one Elf gives you an encrypted 
strategy guide (your puzzle input) that they say will be sure to help you 
win. "The first column is what your opponent is going to play: A for Rock, 
B for Paper, and C for Scissors. The second column--" 

The second column, you reason, must be what you should play in response: 
X for Rock, Y for Paper, and Z for Scissors. Winning every time would be 
suspicious, so the responses must have been carefully chosen.

For example, suppose you were given the following strategy guide:
A Y
B X
C Z

This strategy guide predicts and recommends the following:
- In the first round, your opponent will choose Rock (A), and you should 
choose Paper (Y). This ends in a win for you with a score of 8 (2 because 
you chose Paper + 6 because you won).
- In the second round, your opponent will choose Paper (B), and you should 
choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
- The third round is a draw with both players choosing Scissors, giving 
you a score of 3 + 3 = 6.
"""

from aoc_performance import aoc_perf

ROCK, PAPER, CISORS = 1, 2, 3


def score_outcome(opponent: int, you: int) -> int:
    """Gives score regarding what opponent and you play."""
    if opponent == you:  # draw game
        return 3
    if (
        (opponent == ROCK and you == CISORS)
        or (opponent == PAPER and you == ROCK)
        or (opponent == CISORS and you == PAPER)
    ):  # lose
        return 0
    return 6  # win


def part_A(filename: str) -> int:
    total_score = 0
    hands = {"A": ROCK, "B": PAPER, "C": CISORS, "X": ROCK, "Y": PAPER, "Z": CISORS}
    with open(filename, "r") as f:
        while content := f.readline():
            opponent, you = map(lambda x: hands[x], content.strip().split(" "))
            total_score += you + score_outcome(opponent, you)
    return total_score


def outcome_to_score(outcome: str) -> dict:
    """Tranforms a matrix of outcome to score as dictionary"""
    outcome_dict = {}
    lines = outcome.split("\n")
    header = lines[1]
    for line in lines[2:-1]:  # Remove header and footer
        for i in range(1, 4):
            outcome_dict[line[0] + " " + header[i]] = int(line[i])
    return outcome_dict


def part_A2(filename: str) -> int:
    """Thix matrix shows outcome score when
       You play
    X: rock
    Y: paper
    Z: cisors
    versus
    A: rock
    B: paper
    C: cisors
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
    """Thix matrix shows hand score when
       You
    X: loose hand
    Y: draw hand
    Z: win hand
    versus
    A: rock
    B: paper
    C: cisors
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


def main() -> None:
    # input_filename = "day_02_input_sample.txt"
    input_filename = "day_02_input.txt"

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
