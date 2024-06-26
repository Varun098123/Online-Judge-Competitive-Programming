def parse_card_value(value_str):
    if value_str.isdigit():
        return int(value_str)
    elif value_str == 'T':
        return 10
    elif value_str == 'J':
        return 11
    elif value_str == 'Q':
        return 12
    elif value_str == 'K':
        return 13
    elif value_str == 'A':
        return 14
    else:
        return None


def parse_card(card_str):
    if len(card_str) != 2:
        return None
    value = parse_card_value(card_str[0])
    if value is None:
        return None
    return (value, card_str[1])


def get_hand_rank(hand):
    values = [card[0] for card in hand]
    suits = [card[1] for card in hand]
    values.sort(reverse=True)
    value_counts = {}
    for value in values:
        if value not in value_counts:
            value_counts[value] = 0
        value_counts[value] += 1
    straight_flush = len(set(suits)) == 1 and values == list(range(values[0], values[0] - 5, -1))
    four_of_a_kind = any(count == 4 for count in value_counts.values())
    full_house = set(value_counts.values()) == {2, 3}
    flush = len(set(suits)) == 1
    straight = values == list(range(values[0], values[0] - 5, -1))
    three_of_a_kind = any(count == 3 for count in value_counts.values())
    two_pairs = list(value_counts.values()).count(2) == 2
    one_pair = any(count == 2 for count in value_counts.values())
    if straight_flush:
        return 9, values
    elif four_of_a_kind:
        return 8, values
    elif full_house:
        return 7, values
    elif flush:
        return 6, values
    elif straight:
        return 5, values
    elif three_of_a_kind:
        return 4, values
    elif two_pairs:
        return 3, values
    elif one_pair:
        return 2, values
    else:
        return 1, values


def compare_hands(black_hand, white_hand):
    black_rank, black_values = get_hand_rank(black_hand)
    white_rank, white_values = get_hand_rank(white_hand)
    if black_rank > white_rank:
        return "Black wins."
    elif black_rank < white_rank:
        return "White wins."
    else:
        for i in range(5):
            if black_values[i] > white_values[i]:
                return "Black wins."
            elif white_values[i] > black_values[i]:
                return "White wins."
        return "Tie."


# Input from user
input_lines = []
for i in range(4):
    input_lines.append(input())
for line in input_lines:
    cards = line.split()
    black_hand = [parse_card(card) for card in cards[:5]]
    white_hand = [parse_card(card) for card in cards[5:]]
    print(compare_hands(black_hand, white_hand))
