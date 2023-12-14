from day_13 import (
    DAY,
    part_A,
    part_B,
    read_input,
    find_horizontal_symetry,
    rotate,
    find_vertical_symetry,
    find_horizontal_symetry_block,
    find_vertical_symetry_block,
    modified_array_generator,
)


def test_find_horizontal_symetry():
    arrays = read_input(f"day_{DAY}_input_sample.txt")
    assert find_horizontal_symetry(arrays[0]) == 0
    assert find_horizontal_symetry(arrays[1]) == 4


def test_find_vertical_symetry():
    arrays = read_input(f"day_{DAY}_input_sample.txt")
    assert find_vertical_symetry(arrays[0]) == 5
    assert find_vertical_symetry(arrays[1]) == 0


def test_find_horizontal_symetry_block():
    arrays = read_input(f"day_{DAY}_input_sample.txt")
    assert find_horizontal_symetry_block(arrays[0]) == 0
    assert find_horizontal_symetry_block(arrays[1]) == 4


def test_find_vertical_symetry_block():
    arrays = read_input(f"day_{DAY}_input_sample.txt")
    assert find_vertical_symetry_block(arrays[0]) == 5
    assert find_vertical_symetry_block(arrays[1]) == 0


def test_rotate():
    arrays = read_input(f"day_{DAY}_input_sample.txt")
    assert arrays[0] == rotate(rotate(rotate(rotate(arrays[0]))))

    array = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]
    assert rotate(array) == [["g", "d", "a"], ["h", "e", "b"], ["i", "f", "c"]]


def test_part_A():
    assert part_A(f"day_{DAY}_input_sample.txt") == 405


def test_part_B():
    assert part_B(f"day_{DAY}_input_sample.txt") == 400
