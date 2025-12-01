import day_01 as day


def test_part_A_sample() -> None:
    input_filename = f"day_{day.DAY}_input_sample.txt"
    assert day.part_A(input_filename) == 3


def test_move_part_A() -> None:
    assert day.move_part_A(50, "L", 10) == (40, 0)
    assert day.move_part_A(50, "L", 110) == (40, 0)
    assert day.move_part_A(50, "L", 50) == (0, 1)
    assert day.move_part_A(50, "L", 150) == (0, 1)
    assert day.move_part_A(50, "L", 250) == (0, 1)
    assert day.move_part_A(50, "R", 10) == (60, 0)
    assert day.move_part_A(50, "R", 110) == (60, 0)
    assert day.move_part_A(50, "R", 50) == (0, 1)
    assert day.move_part_A(50, "R", 150) == (0, 1)
    assert day.move_part_A(50, "R", 250) == (0, 1)


def test_move_part_B() -> None:
    assert day.move_part_B(50, "L", 10) == (40, 0)
    assert day.move_part_B(50, "L", 110) == (40, 1)
    assert day.move_part_B(50, "L", 210) == (40, 2)
    assert day.move_part_B(50, "L", 50) == (0, 1)
    assert day.move_part_B(50, "L", 150) == (0, 2)
    assert day.move_part_B(50, "L", 250) == (0, 3)
    assert day.move_part_B(0, "L", 99) == (1, 0)
    assert day.move_part_B(0, "L", 100) == (0, 1)
    assert day.move_part_B(0, "L", 101) == (99, 1)

    assert day.move_part_B(50, "R", 10) == (60, 0)
    assert day.move_part_B(50, "R", 110) == (60, 1)
    assert day.move_part_B(50, "R", 210) == (60, 2)
    assert day.move_part_B(50, "R", 50) == (0, 1)
    assert day.move_part_B(50, "R", 150) == (0, 2)
    assert day.move_part_B(50, "R", 250) == (0, 3)
    assert day.move_part_B(50, "R", 1000) == (50, 10)
    assert day.move_part_B(0, "R", 99) == (99, 0)
    assert day.move_part_B(0, "R", 100) == (0, 1)
    assert day.move_part_B(0, "R", 101) == (1, 1)


def test_part_B_sample() -> None:
    input_filename = f"day_{day.DAY}_input_sample.txt"
    assert day.part_B(input_filename) == 6
