from playingcards import Deck, Card

# 

# player_hand = dummy_deck.draw_n(52)
# player_hand.add_cards(player_deck.draw_n(1), 4, False)
# for x in range(len(player_hand.cards)):
#     print(player_hand.cards[x].img)
# length = 0
Deck_ = globals()["Deck"]

while True == True:
    player_deck = Deck_()
    player_deck.shuffle()
    player_hand = player_deck.draw_n(4)
    while True == True:   
        output = 0
        start = input("Type e for the next card(s), r to reset, q to quit")
        length = len(player_hand.cards)
        if start == 'e':
            if length > 3:
                if player_hand.cards[length-1] == player_hand.cards[length-4]:
                    player_hand.remove_card(length - 1)
                    player_hand.remove_card(length - 2)
                    player_hand.remove_card(length - 3)
                    player_hand.remove_card(length - 4)
                    output = 1
                elif player_hand.cards[length-1].suit_name == player_hand.cards[length - 4].suit_name:
                    player_hand.remove_card(length - 2)
                    player_hand.remove_card(length - 3)
                    output = 2
                else:
                    if player_deck.remaining - 1 < 0:
                        if length > 0:
                            print("Better luck next time!")
                            break
                        else:
                            print("You won!")
                            break
                    player_hand.add_cards(player_deck.draw_n(1), length, False)
                    output = 3
            else:
                if player_deck.remaining - 4-length < 0:
                    if length > 0:
                        print("Better luck next time!")
                        break
                    else:
                        print("You won!")
                        break
                for x in range(4-length):
                    player_hand.add_cards(player_deck.draw_n(1), length, False)
                output = 4
        elif start == "r":
            for x in range(len(player_hand.cards)):
                player_hand.remove_card(0) 
            break
        else:
            exit() 
        for x in range(len(player_hand.cards)):
            print(player_hand.cards[x].img)
        length = len(player_hand.cards)
        match output:
            case 1:
                print("Values match! \n" + str(length) + " Cards in hand " + str(player_deck.remaining) + " Cards in deck")
            case 2:
                print("Suits Match \n" + str(length) + " Cards in hand " + str(player_deck.remaining) + " Cards in deck")
            case 3:
                print("No matches, draw one card \n" + str(length) + " Cards in hand " + str(player_deck.remaining) + " Cards in deck")
            case 4:
                print("Less than 4 cards \n" + str(length) + " Cards in hand " + str(player_deck.remaining) + " Cards in deck")
            case _:
                print("Error")

