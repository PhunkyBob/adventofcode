import pytest
import sys

sys.path.append("..")
from day_09_B import Position, Motions, part_one, part_two

DAY = "09"


def test_position_is_touching():
    pos1 = Position(0, 0)
    pos2 = Position(0, 0)
    assert pos1.is_touching(pos2)
    pos2 = Position(1, 0)
    assert pos1.is_touching(pos2)
    pos2 = Position(0, 1)
    assert pos1.is_touching(pos2)
    pos2 = Position(1, 1)
    assert pos1.is_touching(pos2)
    pos2 = Position(2, 0)
    assert not pos1.is_touching(pos2)


def test_motions_move_head():
    """Tests the head movment."""
    motions = Motions("")
    motions.move_head("R")
    assert motions.knots[0] == Position(1, 0)
    motions.move_head("U")
    assert motions.knots[0] == Position(1, 1)
    motions.move_head("L")
    assert motions.knots[0] == Position(0, 1)
    motions.move_head("D")
    assert motions.knots[0] == Position(0, 0)


def test_motions_move_tail():
    """Tests if the tail folows."""
    motions = Motions("")
    motions.knots[0] = Position(2, 1)
    motions.knots[-1] = Position(1, 1)
    motions.move_head("R")
    assert motions.knots[-1] == Position(2, 1)

    motions.knots[0] = Position(1, 2)
    motions.knots[-1] = Position(1, 3)
    motions.move_head("D")
    assert motions.knots[-1] == Position(1, 2)

    # Move diagonally
    motions.knots[0] = Position(2, 2)
    motions.knots[-1] = Position(1, 1)
    motions.move_head("U")
    assert motions.knots[-1] == Position(2, 2)

    motions.knots[0] = Position(2, 2)
    motions.knots[-1] = Position(1, 1)
    motions.move_head("R")
    assert motions.knots[-1] == Position(2, 2)


def test_motions_move_tail_2():
    """Tests if the tail folows."""
    motions = Motions("", 3)
    motions.knots[0] = Position(2, 1)
    motions.knots[1] = Position(1, 0)
    motions.knots[2] = Position(0, 0)
    motions.move_head("U")
    assert motions.knots[-1] == Position(1, 1)

    motions.move_head("U")
    assert motions.knots[-1] == Position(1, 1)


def test_save_history():
    motions = Motions("")
    for _ in range(4):
        motions.move_head("R")
    assert motions.tail_history[0] == Position(0, 0)
    assert motions.tail_history[1] == Position(0, 0)
    assert motions.tail_history[2] == Position(1, 0)
    assert motions.tail_history[3] == Position(2, 0)
    assert motions.tail_history[4] == Position(3, 0)


def test_motions_get_motions():
    motions = Motions(f"day_{DAY}_input_sample.txt")
    iter = motions.get_motions()
    assert next(iter) == ("R", 4)
    assert next(iter) == ("U", 4)
    assert next(iter) == ("L", 3)


def test_sample_finish_position():
    motions = Motions(f"day_{DAY}_input_sample.txt")
    motions.play()
    assert motions.knots[-1] == Position(1, 2)


def test_part_one():
    input_filename = f"day_{DAY}_input_sample.txt"
    answer = part_one(input_filename)
    assert answer == 13

    input_filename = f"day_{DAY}_input.txt"
    answer = part_one(input_filename)
    assert answer == 6354


if __name__ == "__main__":
    pass
