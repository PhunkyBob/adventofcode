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
from collections import Counter
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
    "J": 1,  # Weakest card
    "Q": 12,
    "K": 13,
    "A": 14,
}


class Hand:
    hand: str
    strenght: HandStrength
    amount: int

    def __init__(self, hand: str, amount: int = 0) -> None:
        self.hand = hand
        self.amount = amount
        self.strenght = self.get_strength(hand)

    def __lt__(self, other: "Hand") -> bool:
        if self.strenght.value != other.strenght.value:
            return self.strenght.value < other.strenght.value
        return next(
            (card_strength[i] < card_strength[j] for i, j in zip(self.hand, other.hand) if i != j),
            False,
        )

    @staticmethod
    def get_strength(hand: str) -> HandStrength:
        if "J" not in hand:
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
        elif not hand.replace("J", ""):
            return HandStrength.FIVE_OF_A_KIND
        else:
            most_frequent_card = Counter(hand.replace("J", "")).most_common(1)[0][0]
            return Hand.get_strength(hand.replace("J", most_frequent_card))


def read_input(input_filename: str) -> List[Hand]:
    hands: List[Hand] = []
    with open(input_filename, "r") as input_file:
        for line in input_file:
            hand, amount = line.strip().split(" ")
            hands.append(Hand(hand, int(amount)))
    return hands


def part_B(input_filename: str) -> int:
    hands = read_input(input_filename)
    hands.sort()
    return sum((rank + 1) * hands[rank].amount for rank in range(len(hands)))


def main() -> None:
    input_filename = f"day_{DAY}_input.txt"
    # input_filename = f"day_{DAY}_input_sample.txt"

    with aoc_perf(memory=True):
        print(f"Day {DAY} Part B")
        answer = part_B(input_filename)
        print(f"Answer: {answer}")
        # Expected result: 254837398


if __name__ == "__main__":
    main()
