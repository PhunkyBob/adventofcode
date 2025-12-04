"""
Advent of Code 2024
--- Day 5: Print Queue ---
https://adventofcode.com/2024/day/5

"""

import functools
from typing import Dict, List, Tuple

from aoc_performance import aoc_perf
from aoc_utils import download_input

DAY = "05"

Ancestors = Dict[int, Tuple[int, ...]]
Update = List[int]


def read_input(input_filename: str):
    with open(input_filename, "r") as file:
        rules_txt, updates_txt = file.read().split("\n\n")
        return process_rules(rules_txt), process_updates(updates_txt)


def add_ancestor(ancestors: Ancestors, key: int, ancestor: int) -> Ancestors:
    ancestors[key] = ancestors[key] + (ancestor,) if key in ancestors else (ancestor,)
    return ancestors


def process_rules(rules_txt: str) -> Tuple[Ancestors, Ancestors]:
    successors: Ancestors = {}
    predecessors: Ancestors = {}
    for line in rules_txt.split("\n"):
        before, after = map(int, line.split("|"))
        successors = add_ancestor(successors, before, after)
        predecessors = add_ancestor(predecessors, after, before)

    return successors, predecessors


def process_updates(updates_txt: str) -> List[Update]:
    return [list(map(int, line.split(","))) for line in updates_txt.split("\n")]


def page_comparison(a: int, b: int, successors: Ancestors, predecessors: Ancestors) -> int:
    if b in successors.get(a, {}) or a in predecessors.get(b, {}):
        return -1
    if a in successors.get(b, {}) or b in predecessors.get(a, {}):
        return 1
    return 0


def reorder_update(update: Update, successors: Ancestors, predecessors: Ancestors) -> Update:
    # comparison_function = functools.partial(page_comparison, successors=successors, predecessors=predecessors)
    # return sorted(update, key=functools.cmp_to_key(comparison_function))
    return sorted(update, key=functools.cmp_to_key(lambda a, b: page_comparison(a, b, successors, predecessors)))


def is_sorted(update: Update, successors: Ancestors, predecessors: Ancestors) -> bool:
    return update == reorder_update(update, successors, predecessors)


def get_middle_element(update: Update) -> int:
    return update[len(update) // 2]


def part_A(input_filename: str) -> int:
    (successors, predecessors), updates = read_input(input_filename)
    return sum(get_middle_element(update) for update in updates if is_sorted(update, successors, predecessors))


def part_B(input_filename: str) -> int:
    (successors, predecessors), updates = read_input(input_filename)
    return sum(
        get_middle_element(reorder_update(update, successors, predecessors))
        for update in updates
        if not is_sorted(update, successors, predecessors)
    )


def main() -> None:
    download_input(DAY, 2024)
    input_filename = f"day_{DAY}_input_sample.txt"
    input_filename = f"day_{DAY}_input.txt"

    with aoc_perf(memory=False):
        print(f"Day {DAY} Part A")
        answer = part_A(input_filename)
        print(f"Answer: {answer}")

    with aoc_perf(memory=False):
        print(f"Day {DAY} Part B")
        answer = part_B(input_filename)
        print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
