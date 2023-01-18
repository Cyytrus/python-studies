'''Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
'''


def value_of_card(card):
    '''Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    '''
    if card in "JQK":
        return 10
    if card == "A":
        return 1
    return int(card)


def higher_card(card_one, card_two):
    '''Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    '''
    val1 = value_of_card(card_one)
    val2 = value_of_card(card_two)
    if val1 == val2:
        return (card_one, card_two)
    if val1 > val2:
        return card_one
    return card_two


def value_of_ace(card_one, card_two):
    '''Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    '''
    val = value_of_hand(card_one, card_two)
    if val < 11:
        return 11
    return 1


def value_of_hand(card_one, card_two):
    '''Determine the value of the hand

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - value of the hand.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    '''
    val = 0
    for card in [card_one, card_two]:
        if card == "A" and val < 11:
            val += 11
        else:
            val += value_of_card(card)
    return val


def is_blackjack(card_one, card_two):
    '''Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    '''
    return value_of_hand(card_one, card_two) == 21


def can_split_pairs(card_one, card_two):
    '''Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    '''
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):
    '''Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    '''
    total = value_of_hand(card_one, card_two)
    if [card_one, card_two].count("A") == 1:
        total -= 10
    return total >= 9 and total <= 11
