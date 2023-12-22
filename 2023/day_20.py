"""
Advent of Code 2023
--- Day 20: Pulse Propagation ---
https://adventofcode.com/2023/day/20

"""
from enum import Enum
from typing import List, Dict, Tuple
from aoc_performance import aoc_perf
from math import lcm

DAY = "20"


class ModuleType(Enum):
    BROADCASTER = 1
    FLIPFLOP = 2
    CONJUNCTION = 3
    OUTPUT = 4


prefix_to_module_type = {
    "b": ModuleType.BROADCASTER,
    "%": ModuleType.FLIPFLOP,
    "&": ModuleType.CONJUNCTION,
    "o": ModuleType.OUTPUT,
}


class Module:
    name: str
    module_type: ModuleType
    destinations: List[str]
    is_on: bool
    remembered_values: Dict[str, bool]

    def __init__(self, input: str) -> None:
        module, dest = input.split(" -> ")
        self.module_type = prefix_to_module_type[module[0]]
        self.name = module.replace("%", "").replace("&", "")
        self.destinations = dest.split(", ")
        self.is_on = False
        self.remembered_values = {}

    def receive(
        self, high_pulse: bool, sender: str = ""
    ) -> List[Tuple[str, bool, str]]:  # module name, hight_pulse, sender
        if self.module_type == ModuleType.BROADCASTER:
            """There is a single broadcast module (named broadcaster).
            When it receives a pulse, it sends the same pulse to all of its destination modules."""
            return [(dest, high_pulse, self.name) for dest in self.destinations]
        if self.module_type == ModuleType.FLIPFLOP and not high_pulse:
            """Flip-flop modules (prefix %) are either on or off; they are initially off.
            If a flip-flop module receives a high pulse, it is ignored and nothing happens.
            However, if a flip-flop module receives a low pulse, it flips between on and off.
            If it was off, it turns on and sends a high pulse. If it was on, it turns off and sends a low pulse."""
            self.is_on = not self.is_on
            return [(dest, self.is_on, self.name) for dest in self.destinations]
        if self.module_type == ModuleType.CONJUNCTION:
            """Conjunction modules (prefix &) remember the type of the most recent pulse received from each of their connected input modules;
            they initially default to remembering a low pulse for each input.
            When a pulse is received, the conjunction module first updates its memory for that input.
            Then, if it remembers high pulses for all inputs, it sends a low pulse; otherwise, it sends a high pulse.
            """
            self.remembered_values[sender] = high_pulse
            new_pulse = not all(self.remembered_values.values())
            return [(dest, new_pulse, self.name) for dest in self.destinations]
        return []


def read_input(input_filename: str) -> Dict[str, Module]:
    with open(input_filename, "r") as input_file:
        m = [Module(line) for line in input_file.read().splitlines()]
    modules: Dict[str, Module] = {module.name: module for module in m}
    # Update all input
    for name, module in modules.items():
        for dest in module.destinations:
            if dest in modules:
                modules[dest].remembered_values[name] = False
    return modules


def press_button(modules: Dict[str, Module], number_of_press: int = 1000) -> int:
    low_pulse_sent = high_pulse_sent = 0
    for _ in range(number_of_press):
        stack: List[Tuple[str, bool, str]] = [("broadcaster", False, "button")]
        while stack:
            dest, pulse, sender = stack.pop(0)
            pulse_txt = "-high-" if pulse else "-low-"
            # print(f"{sender} {pulse_txt}> {dest}")
            if pulse:
                high_pulse_sent += 1
            else:
                low_pulse_sent += 1
            if dest not in modules:
                continue
            stack.extend((dest, pulse, sender) for dest, pulse, sender in modules[dest].receive(pulse, sender))
        # print(low_pulse_sent, high_pulse_sent)
    return low_pulse_sent * high_pulse_sent


def part_A(input_filename: str) -> int:
    modules: Dict[str, Module] = read_input(input_filename)
    return press_button(modules)


def press_button_2(modules: Dict[str, Module], predecessors: Tuple[str, ...]) -> int:
    low_on: Dict[str, int] = {}
    press_no = 0
    while len(low_on) < len(predecessors):
        press_no += 1
        stack: List[Tuple[str, bool, str]] = [("broadcaster", False, "button")]
        while stack:
            dest, pulse, sender = stack.pop(0)
            if dest in predecessors and dest not in low_on and not pulse:
                print(f"{dest} is low on press {press_no+1}")
                low_on[dest] = press_no
            if dest not in modules:
                continue
            stack.extend((dest, pulse, sender) for dest, pulse, sender in modules[dest].receive(pulse, sender))

    return lcm(*low_on.values())


def part_B(input_filename: str) -> int:
    modules: Dict[str, Module] = read_input(input_filename)
    predecessor = "ls"
    predecessors = tuple(module.name for module in modules.values() if predecessor in module.destinations)
    return press_button_2(modules, predecessors)


def main() -> None:
    input_filename = f"day_{DAY}_input.txt"
    # input_filename = f"day_{DAY}_input_sample.txt"
    # input_filename = f"day_{DAY}_input_sample2.txt"

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
