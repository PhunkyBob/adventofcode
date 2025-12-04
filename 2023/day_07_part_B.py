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
from enum import Enum
from typing import Dict, List, Tuple, Union

from aoc_performance import aoc_perf
from aoc_utils import download_input

DAY = "07"


class HandStrength(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIRS = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7


hand_strength: Dict[Union[Tuple, int], HandStrength] = {
    (1, 1, 1, 1, 1): HandStrength.HIGH_CARD,
    (2, 1, 1, 1): HandStrength.ONE_PAIR,
    (2, 2, 1): HandStrength.TWO_PAIRS,
    (3, 1, 1): HandStrength.THREE_OF_A_KIND,
    (3, 2): HandStrength.FULL_HOUSE,
    (4, 1): HandStrength.FOUR_OF_A_KIND,
    (5,): HandStrength.FIVE_OF_A_KIND,
}


def get_card_strength(card: str) -> int:
    order = "J23456789TQKA"
    return order.find(card)


def hand_to_strength(hand: str) -> HandStrength:
    format = tuple(c[1] for c in Counter(hand).most_common())
    return hand_strength[format]


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
            (get_card_strength(i) < get_card_strength(j) for i, j in zip(self.hand, other.hand) if i != j),
            False,
        )

    @staticmethod
    def get_strength(hand: str) -> HandStrength:
        if "J" not in hand:
            return hand_to_strength(hand)
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
    download_input(DAY, 2023)
    input_filename = f"day_{DAY}_input.txt"
    # input_filename = f"day_{DAY}_input_sample.txt"

    with aoc_perf(memory=False):
        print(f"Day {DAY} Part B")
        answer = part_B(input_filename)
        print(f"Answer: {answer}")
        # Expected result: 254837398


if __name__ == "__main__":
    main()
