from day_07_part_B import part_B, Hand, HandStrength


def test_get_strength():
    assert Hand.get_strength("32T3K") == HandStrength.ONE_PAIR
    assert Hand.get_strength("T55J5") == HandStrength.FOUR_OF_A_KIND
    assert Hand.get_strength("KK677") == HandStrength.TWO_PAIRS
    assert Hand.get_strength("KTJJT") == HandStrength.FOUR_OF_A_KIND
    assert Hand.get_strength("QQQJA") == HandStrength.FOUR_OF_A_KIND


def test_hand_comparison():
    assert Hand("T55J5") < Hand("QQQJA")
    assert Hand("QQQJA") < Hand("KTJJT")


def test_part_B():
    assert part_B("day_07_input_sample.txt") == 5905
