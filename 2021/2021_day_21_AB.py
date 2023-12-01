# -*- coding: utf-8 -*-
""" https://adventofcode.com/2021/day/21 """
DAY = "21"


RUN_EACH_TURN = 3


def run_dice() -> int:
    result = 0
    while True:
        result += 1
        yield result


dice = run_dice()


def read_input(filename: str):
    with open(filename, "r") as f:
        initial_positions = [int(line.split(" ")[-1]) for line in map(lambda x: x.strip(), f)]
    return initial_positions


def play(p_pos: int) -> int:
    forward = 0
    for _ in range(RUN_EACH_TURN):
        forward += next(dice)
    return ((p_pos - 1) + forward) % 10 + 1


def part_one(filename: str) -> int:
    positions = read_input(filename)
    scores = [0] * len(positions)
    player = 0
    rolled = 0

    while max(scores) < 1000:
        score = play(positions[player])
        positions[player] = score
        scores[player] += score
        rolled += RUN_EACH_TURN
        player = (player + 1) % 2

    return min(scores) * rolled


def part_two(filename: str) -> int:
    data = read_input(filename)
    # Code
    return


def main() -> None:
    input_filename = f"2021_day_{DAY}_input_sample.txt"
    input_filename = f"2021_day_{DAY}_input.txt"

    print(f"Day {DAY} Part One")
    answer = part_one(input_filename)
    print(f"Answer: {answer}")

    print(f"Day {DAY} Part Two")
    answer = part_two(input_filename)
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
