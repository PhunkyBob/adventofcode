import day_03 as day


def test_part_A_sample() -> None:
    input_filename = f"day_{day.DAY}_input_sample.txt"
    assert day.part_A(input_filename) == 357


def test_max_power_two() -> None:
    array = [int(c) for c in "987654321111111"]
    assert day.max_power_with_two(array) == 98
    array = [int(c) for c in "811111111111119"]
    assert day.max_power_with_two(array) == 89
    array = [int(c) for c in "234234234234278"]
    assert day.max_power_with_two(array) == 78
    array = [int(c) for c in "818181911112111"]
    assert day.max_power_with_two(array) == 92


def test_max_power_general() -> None:
    array = [int(c) for c in "987654321111111"]
    assert day.max_power_general(array, 2) == 98
    array = [int(c) for c in "811111111111119"]
    assert day.max_power_general(array, 2) == 89
    array = [int(c) for c in "234234234234278"]
    assert day.max_power_general(array, 2) == 78
    array = [int(c) for c in "818181911112111"]
    assert day.max_power_general(array, 2) == 92

    array = [int(c) for c in "987654321111111"]
    assert day.max_power_general(array, 12) == 987654321111
    array = [int(c) for c in "811111111111119"]
    assert day.max_power_general(array, 12) == 811111111119
    array = [int(c) for c in "234234234234278"]
    assert day.max_power_general(array, 12) == 434234234278
    array = [int(c) for c in "818181911112111"]
    assert day.max_power_general(array, 12) == 888911112111


def test_part_B_sample() -> None:
    input_filename = f"day_{day.DAY}_input_sample.txt"
    assert day.part_B(input_filename) == 3121910778619
