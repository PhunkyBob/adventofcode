# -*- coding: utf-8 -*-
""" 
--- Day 21: Monkey Math ---
https://adventofcode.com/2022/day/21

root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32

"""
DAY = "21"

from aoc_performance import aoc_perf
from sympy import symbols, solve


def read_input(filename: str):
    data = {}
    with open(filename, "r") as f:
        for line in map(lambda x: x.strip(), f):
            key, value = line.split(": ")
            data[key] = value
    return data


map_operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}


def part_one(filename: str) -> int:
    data = read_input(filename)

    def get_value(key: str) -> int:
        if data[key].isdigit():
            return int(data[key])
        left, operation, right = data[key].split(" ")
        result = int(map_operations[operation](get_value(left), get_value(right)))
        data[key] = result
        return result

    answer = get_value("root")
    return answer


def part_two(filename: str) -> int:
    data = read_input(filename)
    data["root"] = data["root"].replace("+", "-")
    humn = symbols("humn")

    def get_equation(key: str) -> int:
        if key == "humn":
            return "humn"
        if data[key].isdigit() or data[key][0] == "(":
            return data[key]
        left, operation, right = data[key].split(" ")
        result = "(" + get_equation(left) + operation + get_equation(right) + ")"
        data[key] = result
        return result

    equation = get_equation("root")
    answer = solve(eval(equation))
    return int(answer[0])


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
