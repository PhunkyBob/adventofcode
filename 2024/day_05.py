"""
Advent of Code 2024
--- Day 5: Print Queue ---
https://adventofcode.com/2024/day/5

"""

from typing import Any, Callable, Dict, List, Tuple

from aoc_performance import aoc_perf

DAY = "05"

Ancestors = Dict[int, List[int]]
Update = List[int]


def process_rules(rules_txt: str) -> Tuple[Ancestors, Ancestors]:
    successors: Ancestors = {}
    predecessors: Ancestors = {}
    for line in rules_txt.split("\n"):
        before, after = map(int, line.split("|"))
        successors[before] = successors.get(before, []) + [after]
        predecessors[after] = predecessors.get(after, []) + [before]

    return successors, predecessors


def process_updates(updates_txt: str) -> List[Update]:
    return [list(map(int, line.split(","))) for line in updates_txt.split("\n")]


def read_input(input_filename: str):
    with open(input_filename, "r") as file:
        rules_txt, updates_txt = file.read().split("\n\n")
        return process_rules(rules_txt), process_updates(updates_txt)


def is_update_ok(update: Update, successors: Ancestors, predecessors: Ancestors) -> bool:
    for pos in range(len(update) - 1):
        all_before = update[:pos]
        all_after = update[pos + 1 :]
        current = update[pos]
        if any(before in all_after for before in predecessors.get(current, [])) or any(
            after in all_before for after in successors.get(current, [])
        ):
            return False
    return True


def get_middle_element(update: Update) -> int:
    return update[len(update) // 2]


def part_A(input_filename: str) -> int:
    (successors, predecessors), updates = read_input(input_filename)
    return sum(get_middle_element(update) for update in updates if is_update_ok(update, successors, predecessors))


def reorder_update(update: Update, successors: Ancestors, predecessors: Ancestors) -> Update:
    for pos in range(len(update) - 1):
        all_before = update[:pos]
        all_after = update[pos + 1 :]
        current = update[pos]
        for before in predecessors.get(current, []):
            if before in all_after:
                incorrect_index = update.index(before)
                update.insert(pos, update.pop(incorrect_index))
                return reorder_update(update, successors, predecessors)
        for after in successors.get(current, []):
            if after in all_before:
                incorrect_index = all_before.index(after)
                update.insert(incorrect_index + 1, update.pop(pos))
                return reorder_update(update, successors, predecessors)

    return update


def part_B(input_filename: str) -> int:
    (successors, predecessors), updates = read_input(input_filename)
    incorrectly_ordered_updates = [update for update in updates if not is_update_ok(update, successors, predecessors)]
    return sum(
        get_middle_element(reorder_update(update, successors, predecessors)) for update in incorrectly_ordered_updates
    )


def main() -> None:
    input_filename = f"day_{DAY}_input_sample.txt"
    input_filename = f"day_{DAY}_input.txt"

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
