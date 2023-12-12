from day_12 import (
    DAY,
    part_A,
    part_B,
    count_possible_regex,
    count_possible_part2,
    springs_to_tuple,
    size_to_tuple,
    unfold,
)


def test_count_possible():
    assert count_possible_regex("???.###", "1,1,3") == 1
    assert count_possible_regex(".??..??...?##.", "1,1,3") == 4
    assert count_possible_regex("?#?#?#?#?#?#?#?", "1,3,1,6") == 1
    assert count_possible_regex("????.#...#...", "4,1,1") == 1
    assert count_possible_regex("????.######..#####.", "1,6,5") == 4
    assert count_possible_regex("?###????????", "3,2,1") == 10


def test_unfold():
    assert unfold(".#", "?") == ".#?.#?.#?.#?.#"
    assert unfold("1", ",") == "1,1,1,1,1"
    assert unfold("???.###", "?") == "???.###????.###????.###????.###????.###"
    assert unfold("1,1,3", ",") == "1,1,3,1,1,3,1,1,3,1,1,3,1,1,3"


def test_count_possible_part2():
    assert count_possible_part2(springs_to_tuple("???.###"), size_to_tuple("1,1,3")) == 1
    assert count_possible_part2(springs_to_tuple(".??..??...?##."), size_to_tuple("1,1,3")) == 4
    assert count_possible_part2(springs_to_tuple("?#?#?#?#?#?#?#?"), size_to_tuple("1,3,1,6")) == 1
    assert count_possible_part2(springs_to_tuple("????.#...#..."), size_to_tuple("4,1,1")) == 1
    assert count_possible_part2(springs_to_tuple("????.######..#####."), size_to_tuple("1,6,5")) == 4
    assert count_possible_part2(springs_to_tuple("?###????????"), size_to_tuple("3,2,1")) == 10
    assert count_possible_part2(springs_to_tuple("???.###", True), size_to_tuple("1,1,3", True)) == 1
    assert count_possible_part2(springs_to_tuple(".??..??...?##.", True), size_to_tuple("1,1,3", True)) == 16384
    assert count_possible_part2(springs_to_tuple("?#?#?#?#?#?#?#?", True), size_to_tuple("1,3,1,6", True)) == 1
    assert count_possible_part2(springs_to_tuple("????.#...#...", True), size_to_tuple("4,1,1", True)) == 16
    assert count_possible_part2(springs_to_tuple("????.######..#####.", True), size_to_tuple("1,6,5", True)) == 2500
    assert count_possible_part2(springs_to_tuple("?###????????", True), size_to_tuple("3,2,1", True)) == 506250


def test_part_A():
    assert part_A(f"day_{DAY}_input_sample.txt") == 21


def test_part_B():
    assert part_B(f"day_{DAY}_input_sample.txt") == 525152
