import sys

sys.path.append("..")
from day_14_AB import Map, part_one, part_two

DAY = "14"

INPUT_SAMPLE = f"day_{DAY}_input_sample.txt"
INPUT = f"day_{DAY}_input.txt"


def test_init_map():
    map = Map(INPUT_SAMPLE)
    assert map.is_occupied(500, 0) == False
    assert map.is_occupied(498, 4) == True
    assert map.is_occupied(496, 6) == True
    assert map.is_occupied(494, 9) == True


def test_drop_sand():
    map = Map(INPUT_SAMPLE)
    res = map.drop_sand()
    assert res == True
    assert (500, 8) in map.occupied


def test_part_one():
    assert part_one(INPUT_SAMPLE) == 24
    assert part_one(INPUT) == 828


def test_part_two():
    assert part_two(INPUT_SAMPLE) == 93
    assert part_two(INPUT) == 25500


if __name__ == "__main__":
    pass
