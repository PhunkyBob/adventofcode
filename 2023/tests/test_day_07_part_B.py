from day_07_part_B import part_B, Hand, HandStrength, hand_to_strength


def test_hand_to_strength():
    assert hand_to_strength("23456") == HandStrength.HIGH_CARD
    assert hand_to_strength("22345") == HandStrength.ONE_PAIR
    assert hand_to_strength("12234") == HandStrength.ONE_PAIR
    assert hand_to_strength("22334") == HandStrength.TWO_PAIRS
    assert hand_to_strength("12233") == HandStrength.TWO_PAIRS
    assert hand_to_strength("22344") == HandStrength.TWO_PAIRS
    assert hand_to_strength("22234") == HandStrength.THREE_OF_A_KIND
    assert hand_to_strength("12223") == HandStrength.THREE_OF_A_KIND
    assert hand_to_strength("22233") == HandStrength.FULL_HOUSE
    assert hand_to_strength("22333") == HandStrength.FULL_HOUSE
    assert hand_to_strength("22223") == HandStrength.FOUR_OF_A_KIND
    assert hand_to_strength("12222") == HandStrength.FOUR_OF_A_KIND
    assert hand_to_strength("22222") == HandStrength.FIVE_OF_A_KIND

    assert hand_to_strength("32T3K") == HandStrength.ONE_PAIR
    assert hand_to_strength("T55J5") == HandStrength.THREE_OF_A_KIND
    assert hand_to_strength("KK677") == HandStrength.TWO_PAIRS
    assert hand_to_strength("KTJJT") == HandStrength.TWO_PAIRS
    assert hand_to_strength("QQQJA") == HandStrength.THREE_OF_A_KIND


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
