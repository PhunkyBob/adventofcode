"""
Advent of Code 2023
--- Day 7: Camel Cards ---
https://adventofcode.com/2023/day/7

To play Camel Cards, you are given a list of hands and their corresponding bid (your puzzle input). For example:

32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""
from typing import List, Dict
from aoc_performance import aoc_perf
from enum import Enum
import re

DAY = "07"


class HandStrength(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIRS = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7


card_strength: Dict[str, int] = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}


class Hand:
    hand: str
    strength: HandStrength
    amount: int

    def __init__(self, hand: str, amount: int = 0) -> None:
        self.hand = hand
        self.amount = amount
        self.strength = self.get_strength(hand)

    def __lt__(self, other: "Hand") -> bool:
        if self.strength.value != other.strength.value:
            return self.strength.value < other.strength.value
        return next(
            (
                card_strength[self.hand[i]] < card_strength[other.hand[i]]
                for i in range(len(self.hand))
                if card_strength[self.hand[i]] != card_strength[other.hand[i]]
            ),
            False,
        )

    @staticmethod
    def get_strength(hand: str) -> HandStrength:
        sorted_hand = "".join(sorted(hand))
        if re.search(r"(.)\1{4}", sorted_hand):
            return HandStrength.FIVE_OF_A_KIND
        if re.search(r"(.)\1{3}", sorted_hand):
            return HandStrength.FOUR_OF_A_KIND
        if re.search(r"(.)\1{2}(.)\2", sorted_hand) or re.search(r"(.)\1(.)\2{2}", sorted_hand):
            return HandStrength.FULL_HOUSE
        if re.search(r"(.)\1{2}", sorted_hand):
            return HandStrength.THREE_OF_A_KIND
        if re.search(r"(.)\1.?(.)\2", sorted_hand):
            return HandStrength.TWO_PAIRS
        if re.search(r"(.)\1", sorted_hand):
            return HandStrength.ONE_PAIR
        return HandStrength.HIGH_CARD


def read_input(input_filename: str) -> List[Hand]:
    hands: List[Hand] = []
    with open(input_filename, "r") as input_file:
        for line in input_file:
            hand, amount = line.strip().split(" ")
            hands.append(Hand(hand, int(amount)))
    return hands


def part_A(input_filename: str) -> int:
    hands = read_input(input_filename)
    hands.sort()
    return sum((rank + 1) * hands[rank].amount for rank in range(len(hands)))


def main() -> None:
    input_filename = f"day_{DAY}_input.txt"
    # input_filename = f"day_{DAY}_input_sample.txt"

    with aoc_perf(memory=True):
        print(f"Day {DAY} Part A")
        answer = part_A(input_filename)
        print(f"Answer: {answer}")
        # Expected result: 253954294


if __name__ == "__main__":
    main()
