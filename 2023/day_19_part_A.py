"""
Advent of Code 2023
--- Day 19: Aplenty ---
https://adventofcode.com/2023/day/19

"""
from operator import mul
from typing import Any, Callable, List, Dict, Tuple
from aoc_performance import aoc_perf
import re
import functools


DAY = "19"
Condition = Tuple[int, Callable, int, str]  # elem to test, test function, limit value, next state if true
Workflow = List[Condition]
Part = Tuple[int, int, int, int]  # x, m, a,s
test_lt = lambda x, y: x < y
test_gt = lambda x, y: x > y
always_true = lambda x, y: True


def process_rules(rules_txt: str) -> Dict[str, Workflow]:
    corresponding_rules: Dict[str, Callable] = {"<": test_lt, ">": test_gt}
    workflows: Dict[str, Workflow] = {}
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
                elem_to_test = "xmas".find(elem_to_test)
                condition: Condition = (
                    elem_to_test,
                    corresponding_rules[test_function],
                    int(limit_value),
                    next_state_if_true,
                )
            else:
                # default rule
                condition: Condition = (0, always_true, 0, item)
            workflow.append(condition)
        workflows[name] = workflow
    return workflows


def process_parts(parts_txt: str) -> List[Part]:
    return [tuple(list(map(int, re.findall(r"\d+", part)))) for part in parts_txt.split("\n")]  # type: ignore


def read_input(input_filename: str) -> Tuple[Dict[str, Workflow], List[Part]]:
    with open(input_filename, "r") as f:
        rules_txt, parts_txt = f.read().split("\n\n")
        workflows: Dict[str, Workflow] = process_rules(rules_txt)
        parts: List[Part] = process_parts(parts_txt)
    return workflows, parts


def find_final_state(from_state: str, part: Part, workflows: Dict[str, Workflow]) -> str:
    current_state = from_state
    while current_state not in ["R", "A"]:
        workflow: Workflow = workflows[current_state]
        for elem_to_test, test_function, limit_value, next_state_if_true in workflow:
            if test_function(part[elem_to_test], limit_value):
                current_state = next_state_if_true
                # print(f"current_state: {current_state}")
                break
    return current_state


def part_A(input_filename: str) -> int:
    workflows, parts = read_input(input_filename)
    return sum(
        part[0] + part[1] + part[2] + part[3] for part in parts if find_final_state("in", part, workflows) == "A"
    )


def main() -> None:
    input_filename = f"day_{DAY}_input.txt"
    # input_filename = f"day_{DAY}_input_sample.txt"

    with aoc_perf(memory=False):
        print(f"Day {DAY} Part A")
        answer = part_A(input_filename)
        print(f"Answer: {answer}")
        # Expected answer: 368523


if __name__ == "__main__":
    main()
