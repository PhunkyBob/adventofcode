from day_10 import (
    part_A,
    part_B,
    Pipe,
    Direction,
    get_opposite_direction,
    pipe_to_directions,
    get_starting_pipes,
    read_input,
)


def test_pipe_to_directions():
    assert Pipe("|").connections == {Direction.NORTH, Direction.SOUTH}
    assert Pipe("-").connections == {Direction.EAST, Direction.WEST}
    assert Pipe("L").connections == {Direction.NORTH, Direction.EAST}
    assert Pipe("J").connections == {Direction.NORTH, Direction.WEST}
    assert Pipe("7").connections == {Direction.SOUTH, Direction.WEST}
    assert Pipe("F").connections == {Direction.SOUTH, Direction.EAST}
    assert Pipe(".").connections == set()
    assert Pipe("S").connections == {Direction.NORTH, Direction.SOUTH, Direction.EAST, Direction.WEST}


def test_is_connected():
    assert Pipe("|").is_connected(Pipe("|"), Direction.NORTH)
    assert Pipe("|").is_connected(Pipe("|"), Direction.SOUTH)
    assert not Pipe("|").is_connected(Pipe("|"), Direction.EAST)
    assert not Pipe("|").is_connected(Pipe("|"), Direction.WEST)
    assert Pipe("-").is_connected(Pipe("-"), Direction.EAST)
    assert Pipe("-").is_connected(Pipe("-"), Direction.WEST)
    assert not Pipe("-").is_connected(Pipe("-"), Direction.NORTH)
    assert not Pipe("-").is_connected(Pipe("-"), Direction.SOUTH)
    assert not Pipe("L").is_connected(Pipe("L"), Direction.NORTH)
    assert Pipe("L").is_connected(Pipe("7"), Direction.EAST)
    assert Pipe("L").is_connected(Pipe("7"), Direction.NORTH)
    assert not Pipe("L").is_connected(Pipe("7"), Direction.SOUTH)


def test_get_starting_pipes():
    assert get_starting_pipes(read_input("day_10_input_sample.txt")) == (1, 1)
    assert get_starting_pipes(read_input("day_10_input_sample2.txt")) == (2, 0)


def test_part_A():
    assert part_A("day_10_input_sample.txt") == 4
    assert part_A("day_10_input_sample2.txt") == 8


def test_part_B():
    assert part_B("day_10_input_sample3.txt") == 4
    assert part_B("day_10_input_sample4.txt") == 8
    assert part_B("day_10_input_sample5.txt") == 10
