import random
print(" ==== Blackjack ==== \n")

#suits inside of deck
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4
suits = ["Spades", "Diamonds", "Hearts", "Clubs"] * 13

print(cards)

counter = 0
players_hand = []
players_suit = []
players_chips = 10
dealers_hand = []
dealers_suit = []
players_hand_value = 0
dealers_hand_value = 0
players_bet = 0
loop_counter = 1
player_round_finished = False
print(len(cards))

for suit in suits:
    for card in cards:
        if counter < 2:
            drawn_suit = random.choice(list(suits))
            drawn_card = random.choice(list(cards))

            dealers_hand.append(drawn_card)
            cards.remove(drawn_card)
            suits.remove(drawn_suit)
            counter += 1

print(f"Dealers revealed card is: {dealers_hand[0]} of {drawn_suit}")

print("your hand is:")
for suit in suits:
    for card in cards:
        if counter < 25:
            drawn_suit = random.choice(list(suits))
            drawn_card = random.choice(list(cards))

            players_hand.append(drawn_card)
            cards.remove(drawn_card)
            suits.remove(drawn_suit)
            print(f"{drawn_card} of {drawn_suit}")
            counter += 1
        else:
            break
print(f"start round:Players hand: {players_hand}")

