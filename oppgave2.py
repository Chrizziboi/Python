import random

print(" ==== Blackjack ==== \n")
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4
suits = ["Spades", "Diamonds", "Hearts", "Clubs"]

players_hand = []
players_suit = []
dealers_hand = []
dealers_suit = []

username = None
counter = 0
players_chips = 10
players_hand_value = 0
dealers_hand_value = 0
players_bet = 0
restart = 0
loop_counter = 1

player_round_finished = False
in_play = True
while in_play == True:

    def start():
        global players_chips
        global in_play
        global player_round_finished
        global loop_counter
        global players_bet
        global cards

        motivational_message = ["you got this!", "Go get 'em!", "never give up!", "ready, set, go!"]
        counter = 0

        if players_chips <= 0:
            print("It seems you've run out of chips!\n")
            return stop()

        elif len(cards) == 0 and players_chips > 0:
            print("There are no more cards in the deck, starting over with a full deck of cards.\n")
            cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4

        else:
            players_bet = int(input(f"You currently have {players_chips} chips,\n"
                                    f"How many chips do you want to bet?: "))

            if players_bet > players_chips:
                print("\nYou don't have that many chips!\n"
                      "please, choose a lower amount within your chip range!\n")
                start()

            print(f"\n{random.choice(list(motivational_message))} get ready for round {loop_counter}:")
            loop_counter += 1
            players_hand.clear()
            dealers_hand.clear()
            player_round_finished = False
            print("\nDealing ... \n")

            for k in cards, suits:
                if counter < 2:
                    drawn_suit = random.choice(list(suits))
                    drawn_card = random.choice(list(cards))

                    dealers_hand.append(drawn_card)
                    cards.remove(drawn_card)

                    counter += 1

            print(f"Dealers revealed card is: {dealers_hand[0]} of {drawn_suit}")
            print("your hand is:")

            for k in cards, suits:

                if counter < 4:
                    drawn_suit = random.choice(list(suits))
                    drawn_card = random.choice(list(cards))

                    players_hand.append(drawn_card)
                    cards.remove(drawn_card)
                    print(f"{drawn_card} of {drawn_suit}")
                    counter += 1
                else:
                    break
            print(f"\nThere are {len(cards)} cards in the deck remaining.\n")
        return decision()

    def decision():
        global players_chips
        global in_play
        global player_round_finished
        global player_choice
        global players_bet

        if len(cards) <= 0:
            return stop()

        players_hand_value = sum(players_hand)
        dealers_hand_value = sum(dealers_hand)
        if player_round_finished == True:
            print(
                f"You choose to stand with a hand value of {players_hand_value}.\nDealer is finished drawing cards, ending"
                f" with a total hand value of {dealers_hand_value}.\n")
            if players_hand_value == dealers_hand_value and dealers_hand_value <= 21:
                print(f"You both have the same card value! {username}: card value of:{players_hand_value}\n "
                      f"and Dealers card value of: {dealers_hand_value}. nobody wins, but you get your chips back.\n")
                start()
            elif players_hand_value > 21 and dealers_hand_value <= 21:
                print(
                    f"{username} bust! your hands value is {players_hand_value} and dealer has a value of {dealers_hand_value}.\n")
                players_chips -= players_bet
                start()
            elif dealers_hand_value > 21 and players_hand_value <= 21:
                print(f"Dealer bust! dealer has a hand value of {dealers_hand_value}, {username} wins with "
                      f"a hand value of {players_hand_value}.\n")
                players_chips += players_bet * 2
                start()
            elif players_hand_value == 21 and dealers_hand_value != 21:
                print(f"{username} have blackjack! and dealers has a card value of {dealers_hand_value}, \n"
                      f"{username} earns {players_bet * 2}")
                players_chips += players_bet * 2
                start()
            elif dealers_hand_value == 21 and players_hand_value != 21:
                print(f"Dealer has Blacjack! {username} loses {players_bet} chips.\n")
                players_chips -= players_bet
                start()
            elif players_hand_value < dealers_hand_value:
                print(f"{username} loses, Dealer has a higher value.\n")
                players_chips -= players_bet
                start()
            elif players_hand_value > dealers_hand_value:
                print(f"{username} wins! Dealer has a lower value!\n")
                players_chips += players_bet
                start()
            elif dealers_hand_value <= 10 and [1] in dealers_hand:
                dealers_hand[1] = 11
        elif players_hand_value == 21:
            print(f"{username} has blackjack! \n"
                  f"{username} earns {players_bet * 2}")
            players_chips += players_bet * 2
            start()
        elif players_hand_value > 21:
            print(f"{username} busts! {username} hands value is {players_hand_value}.")
            players_chips -= players_bet
            start()

        else:
            player_choice = int(input(f"{username}s total hand value is: {players_hand_value}, what would you like to do?:\n"
                                      f"1 - hit\n or\n2 - stand\nPlease write here(only the number): "))
        if player_choice > 2 or player_choice <= 0:
            print('You need to input 1 or 2 ')
            decision()
        elif player_choice == 1:
            print("you choose to hit!")
            deal()
        elif player_choice == 2:
            print("You choose to stand!")
            player_round_finished = True
            deal()

        return decision()

    def deal():
        global in_play
        if players_chips <= 0 or len(cards) <= 0:
            return stop()
        counter = 0
        print("\nShuffling ... \n")

        print("\nDealing ... \n")

        for k in cards, suits:
            if counter < 1:
                if players_hand_value < 21 and player_round_finished == False:
                    drawn_suit = random.choice(list(suits))
                    drawn_card = random.choice(list(cards))
                    players_hand.append(drawn_card)
                    print(f"{drawn_card} of {drawn_suit}")
                    cards.remove(drawn_card)
                    counter += 1
            else:
                break
            dealers_hand_value = sum(dealers_hand)
            for k in cards, suits:
                if dealers_hand_value < 17 and player_round_finished == True:
                    drawn_suit = random.choice(list(suits))
                    drawn_card = random.choice(list(cards))
                    dealers_hand.append(drawn_card)
                    cards.remove(drawn_card)
                    print(f"Dealer draws: {drawn_card} of {drawn_suit}")
        print(f"\nThere are {len(cards)} cards in the deck remaining.\n")
        return decision()

    def stop():
        global loop_counter
        global in_play
        global players_chips
        global username
        global restart
        global cards

        if loop_counter > 1 and players_chips <= 0:
            restart = int(input(f"\nThanks for playing Blackjack {username}! you have no more chips to play with!\n"
                                f"Do you want to play again? 1 for yes, 2 for no.\n:"))
            if restart > 2 or restart < 0:
                print("\nyou seem to have typed something wrong, please choose between 1 and 2.\n")
            elif restart == 1:
                print("\nOkey! Restarting, giving you 10 chips to play with.")
                players_chips = 10
                loop_counter = 1
                cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4
                start()
            elif restart == 2:
                print(f"See you again {username}! \nnow exiting...")
                in_play = False
                exit()
            else:
                return in_play == False
        else:
            return in_play == False

    if loop_counter == 1 and in_play == True:
        username = input("Welcome to Blackjack! write your username here: ")
        print(f"Hello {username}, lets begin round {loop_counter}!")
        start()
    else:
        break
exit()

Myvar = "malla"
