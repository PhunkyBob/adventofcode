import pytest
import sys

sys.path.append("..")
from day_11_AB import Monkey, MonkeysPack, part_one, part_two

DAY = "11"

INPUT_SAMPLE = f"day_{DAY}_input_sample.txt"
INPUT = f"day_{DAY}_input.txt"


def test_init_monkey():
    monkey_txt = """
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3
    """

    monkey = Monkey(monkey_txt)
    assert monkey.id == 0
    assert len(monkey.items) == 2
    assert monkey.items[0] == 79
    assert monkey.items[1] == 98
    assert monkey.operation(1) == 19
    assert monkey.throw_to_monkey(23) == 2
    assert monkey.throw_to_monkey(1) == 3

    monkey_txt = """
Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3
    """
    monkey = Monkey(monkey_txt)
    assert monkey.operation(1) == 1
    assert monkey.operation(10) == 100


def test_init_monkeys_pack():
    pack = MonkeysPack(INPUT_SAMPLE)
    assert len(pack.monkeys) == 4
    assert pack.monkeys[-1].id == 3


def test_monkey_cool_down():
    assert Monkey.cool_down(1501) == 500


def test_play_round():
    pack = MonkeysPack(INPUT_SAMPLE, True)
    pack.play_round()
    assert pack.monkeys[0].items == [20, 23, 27, 26]
    assert pack.monkeys[1].items == [2080, 25, 167, 207, 401, 1046]
    assert pack.monkeys[2].items == []
    assert pack.monkeys[3].items == []


def test_inspection_count():
    pack = MonkeysPack(INPUT_SAMPLE, True)
    for _ in range(20):
        pack.play_round()
    assert pack.monkeys[0].inspection_count == 101
    assert pack.monkeys[1].inspection_count == 95
    assert pack.monkeys[2].inspection_count == 7
    assert pack.monkeys[3].inspection_count == 105


def test_part_one():
    answer = part_one(INPUT_SAMPLE)
    assert answer == 10605
    answer = part_one(INPUT)
    assert answer == 50172


if __name__ == "__main__":
    pass
