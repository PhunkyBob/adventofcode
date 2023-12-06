from day_06 import part_A, part_B, count_winning_loop, count_winning_math


def test_count_winning():
    assert count_winning_loop(7, 9) == 4
    assert count_winning_loop(15, 40) == 8
    assert count_winning_loop(30, 200) == 9


def test_count_winning_math():
    assert count_winning_math(7, 9) == 4
    assert count_winning_math(15, 40) == 8
    assert count_winning_math(30, 200) == 9


def test_part_A():
    assert part_A("day_06_input_sample.txt") == 288


def test_part_B():
    assert part_B("day_06_input_sample.txt") == 71503
