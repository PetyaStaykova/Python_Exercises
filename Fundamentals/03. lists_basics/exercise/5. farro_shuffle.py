deck_of_cards = input().split()
n_shuffles = int(input())
half_deck = len(deck_of_cards) // 2


for i in range(n_shuffles):
    left_deck = deck_of_cards[0:half_deck]
    right_deck = deck_of_cards[half_deck:]
    shuffled_deck = []
    for card in range(len(left_deck)):
        shuffled_deck.append(left_deck[card])
        shuffled_deck.append(right_deck[card])
    deck_of_cards = shuffled_deck

print(deck_of_cards)