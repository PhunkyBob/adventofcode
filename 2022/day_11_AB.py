# -*- coding: utf-8 -*-
""" 
--- Day 11: Monkey in the Middle ---
https://adventofcode.com/2022/day/11

You need to be able to predict where the monkeys 
will throw your items. After some careful observation, you realize the 
monkeys operate based on how worried you are about each item.

Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

"""
DAY = "11"

from aoc_performance import aoc_perf
from typing import List
import re
import heapq
from functools import reduce


class Monkey:
    id: int
    items: List[int]
    operation: callable
    operation_name: str
    operation_value: str
    throw_to_monkey: callable
    throw_to_monkey_test_value: int
    inspection_count: int = 0

    def __init__(self, monkey_txt: str) -> None:
        self.inspection_count = 0
        res = re.search("Monkey (\d+):", monkey_txt)
        self.id = int(res[1])
        res = re.search("Starting items: (.+)", monkey_txt)
        self.items = list(map(int, res[1].split(", ")))
        res = re.search("Operation: new = old (.+) (.+)", monkey_txt)
        if res[2] == "old":
            self.operation = lambda x: x * x
            self.operation_name = "multiplied"
            self.operation_value = "itself"
        else:
            if res[1] == "+":
                self.operation = lambda x: x + int(res[2])
                self.operation_name = "increased"
                self.operation_value = res[2]
            elif res[1] == "*":
                self.operation = lambda x: x * int(res[2])
                self.operation_name = "multiplied"
                self.operation_value = res[2]
            else:
                self.operation = lambda x: x
                self.operation_name = "???"
                self.operation_value = "???"
        res_test = re.search("Test: divisible by (\d+)", monkey_txt)
        self.throw_to_monkey_test_value = int(res_test[1])
        res_true = re.search("If true: throw to monkey (\d+)", monkey_txt)
        res_false = re.search("If false: throw to monkey (\d+)", monkey_txt)
        self.throw_to_monkey = (
            lambda x: int(res_true[1]) if x % self.throw_to_monkey_test_value == 0 else int(res_false[1])
        )

    @staticmethod
    def cool_down(worry_level: int):
        return worry_level // 3


class MonkeysPack:
    monkeys: List[Monkey]
    debug: bool

    def __init__(self, filename: str, debug=False) -> None:
        self.monkeys = []
        with open(filename, "r") as f:
            for monkey_txt in f.read().split("\n\n"):
                self.monkeys.append(Monkey(monkey_txt))
        self.debug = debug

    def play_round(self):
        for monkey in self.monkeys:
            if self.debug:
                print(f"Monkey {monkey.id}")
            while len(monkey.items):
                monkey.inspection_count += 1
                item = monkey.items.pop(0)
                worry_level = monkey.operation(item)
                new_worry_level = monkey.cool_down(worry_level)
                monkey_to_throw = monkey.throw_to_monkey(new_worry_level)
                self.monkeys[monkey_to_throw].items.append(new_worry_level)
                if self.debug:
                    print(f"  Monkey inspects an item with a worry level of {item}.")
                    print(f"    Worry level is {monkey.operation_name} by {monkey.operation_value} to {worry_level}.")
                    print(f"    Monkey gets bored with item. Worry level is divided by 3 to {new_worry_level}.")
                    print(f"    Test if worry level is divisible by {monkey.throw_to_monkey_test_value}.")
                    print(f"    Item with worry level {new_worry_level} is thrown to monkey {monkey_to_throw}.")


def part_one(filename: str) -> int:
    pack = MonkeysPack(filename, False)
    for _ in range(20):
        pack.play_round()
    top_n = heapq.nlargest(2, pack.monkeys, key=lambda x: x.inspection_count)
    answer = reduce(lambda x, y: x.inspection_count * y.inspection_count, top_n)
    return answer


def part_two(filename: str) -> int:
    # Code
    return


def main() -> None:
    input_filename = f"day_{DAY}_input_sample.txt"
    input_filename = f"day_{DAY}_input.txt"

    with aoc_perf():
        print(f"Day {DAY} Part One")
        answer = part_one(input_filename)
        print(f"Answer: {answer}")

    with aoc_perf():
        print(f"Day {DAY} Part Two")
        answer = part_two(input_filename)
        print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
