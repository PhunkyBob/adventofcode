"""
Advent of Code 2023
--- Day 19: Aplenty ---
https://adventofcode.com/2023/day/19

"""
from operator import mul
from typing import List, Dict, Tuple
from aoc_performance import aoc_perf
import re
import functools


DAY = "19"
Condition = Tuple[str, str, int, str]  # elem to test, test condition, limit value, next state if true
Workflow = List[Condition]


workflows: Dict[str, Workflow] = {}


def load_input(input_filename: str) -> None:
    global workflows
    with open(input_filename, "r") as f:
        rules_txt, _ = f.read().split("\n\n")
        workflows = {}
        for rule in rules_txt.split("\n"):
            if res := re.match(r"([a-zA-Z]+){(.+)}", rule):
                name, workflow_txt = res.groups()
            else:
                raise ValueError(f"Cannot parse rule: {rule}")
            workflow: Workflow = []
            for item in workflow_txt.split(","):
                if res := re.match(r"([a-zA-Z])([<>])(\d+):([a-zA-Z]+)", item):
                    # Conditional rule
                    elem_to_test, test_function, limit_value, next_state_if_true = res.groups()
                    condition: Condition = (
                        elem_to_test,
                        test_function,
                        int(limit_value),
                        next_state_if_true,
                    )
                else:
                    # default rule
                    condition: Condition = ("x", ">", 0, item)
                workflow.append(condition)
            workflows[name] = workflow
    return


def run_tree(state: str, bounds: Dict[str, Tuple[int, int]]) -> int:
    if state == "R":
        return 0
    if state == "A":
        return functools.reduce(mul, [elem[1] - elem[0] + 1 for elem in bounds.values()])
    total = 0
    for elem_to_test, test_function, limit_value, next_state_if_true in workflows[state]:
        if test_function == ">":
            new_bounds = bounds.copy()
            new_bounds[elem_to_test] = (max(bounds[elem_to_test][0], limit_value + 1), bounds[elem_to_test][1])
            total += run_tree(next_state_if_true, new_bounds)
            bounds[elem_to_test] = (bounds[elem_to_test][0], min(bounds[elem_to_test][1], limit_value))
        elif test_function == "<":
            new_bounds = bounds.copy()
            new_bounds[elem_to_test] = (bounds[elem_to_test][0], min(bounds[elem_to_test][1], limit_value - 1))
            total += run_tree(next_state_if_true, new_bounds)
            bounds[elem_to_test] = (max(bounds[elem_to_test][0], limit_value), bounds[elem_to_test][1])
    return total


def part_B(input_filename: str) -> int:
    load_input(input_filename)
    return run_tree("in", {elem: (1, 4000) for elem in "xmas"})


def main() -> None:
    input_filename = f"day_{DAY}_input.txt"
    # input_filename = f"day_{DAY}_input_sample.txt"

    with aoc_perf(memory=True):
        print(f"Day {DAY} Part B")
        answer = part_B(input_filename)
        print(f"Answer: {answer}")
        # Expected answer: 124167549767307


if __name__ == "__main__":
    main()
