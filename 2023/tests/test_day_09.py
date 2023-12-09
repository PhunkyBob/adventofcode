from day_09 import part_A, part_B, get_sequence, get_last_extrapolated_value


def test_get_sequence():
    assert get_sequence([0, 3, 6, 9, 12, 15]) == [[0, 3, 6, 9, 12, 15], [3, 3, 3, 3, 3], [0, 0, 0, 0]]
    assert get_sequence([1, 3, 6, 10, 15, 21]) == [[1, 3, 6, 10, 15, 21], [2, 3, 4, 5, 6], [1, 1, 1, 1], [0, 0, 0]]
    assert get_sequence([10, 13, 16, 21, 30, 45]) == [
        [10, 13, 16, 21, 30, 45],
        [3, 3, 5, 9, 15],
        [0, 2, 4, 6],
        [2, 2, 2],
        [0, 0],
    ]


def test_get_extrapolated_value():
    assert get_last_extrapolated_value([[0, 3, 6, 9, 12, 15], [3, 3, 3, 3, 3], [0, 0, 0, 0]]) == 18
    assert get_last_extrapolated_value([[1, 3, 6, 10, 15, 21], [2, 3, 4, 5, 6], [1, 1, 1, 1], [0, 0, 0]]) == 28
    assert (
        get_last_extrapolated_value([[10, 13, 16, 21, 30, 45], [3, 3, 5, 9, 15], [0, 2, 4, 6], [2, 2, 2], [0, 0]])
        == 68
    )


def test_part_A():
    assert part_A("day_09_input_sample.txt") == 114


def test_part_B():
    assert part_B("day_09_input_sample.txt") == 2
