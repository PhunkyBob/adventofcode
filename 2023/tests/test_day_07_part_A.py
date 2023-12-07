from day_07_part_A import part_A, Hand, HandStrength


def test_get_strength():
    assert Hand.get_strength("23456") == HandStrength.HIGH_CARD
    assert Hand.get_strength("22345") == HandStrength.ONE_PAIR
    assert Hand.get_strength("12234") == HandStrength.ONE_PAIR
    assert Hand.get_strength("22334") == HandStrength.TWO_PAIRS
    assert Hand.get_strength("12233") == HandStrength.TWO_PAIRS
    assert Hand.get_strength("22344") == HandStrength.TWO_PAIRS
    assert Hand.get_strength("22234") == HandStrength.THREE_OF_A_KIND
    assert Hand.get_strength("12223") == HandStrength.THREE_OF_A_KIND
    assert Hand.get_strength("22233") == HandStrength.FULL_HOUSE
    assert Hand.get_strength("22333") == HandStrength.FULL_HOUSE
    assert Hand.get_strength("22223") == HandStrength.FOUR_OF_A_KIND
    assert Hand.get_strength("12222") == HandStrength.FOUR_OF_A_KIND
    assert Hand.get_strength("22222") == HandStrength.FIVE_OF_A_KIND

    assert Hand.get_strength("32T3K") == HandStrength.ONE_PAIR
    assert Hand.get_strength("T55J5") == HandStrength.THREE_OF_A_KIND
    assert Hand.get_strength("KK677") == HandStrength.TWO_PAIRS
    assert Hand.get_strength("KTJJT") == HandStrength.TWO_PAIRS
    assert Hand.get_strength("QQQJA") == HandStrength.THREE_OF_A_KIND


def test_hand_comparison():
    assert Hand("23456") < Hand("34567")
    assert Hand("23456") < Hand("23467")
    assert Hand("23456") < Hand("23457")
    assert Hand("QQQJA") < Hand("A55J5")


def test_part_A():
    assert part_A("day_07_input_sample.txt") == 6440
