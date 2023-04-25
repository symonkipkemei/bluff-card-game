import random
import time

from parameters import *


def bluff():
    while True:
        user_choice =str(input("Call bluff ? (y/n): "))
        if user_choice == str.lower("y"):
            return True
            break
        elif user_choice == str.lower("n"):
            return False
            break
        else:
            print("wrong input try again")

        
def bluff_outcome(last_card, card_choice,ans = True):
    if ans is True and not None:
        # check oppoonents card
        print(f"last_card:{last_card}")
        print(f"card played:{card_choice}")

        if card_choice == last_card:
            print("It is not a bluff, you got it wrong!")
            #  move deck to the appropiate person, with exception of the last card
        else:
            print("Its a bluff!")
            #  move deck to the appropiate person, with exception of the last card

def main():
    #objects are identified
    deck = Deck()

    # welcome

    print("WELCOME TO THE BLUFF GAME \nIf you are not cheating you are not trying hard enough\nEnjoy!\n")


    # cards shuffled

    print("Cards are shuffled")
    time.sleep(3)
    deck.shuffle()
  
    print("\nshuffling is complete\n")
    

    # playing hands are identified
    print("\nPlayers are identified\n")
    time.sleep(3)


    computer_hand = Hand("computer")
    human_hand = Hand("symon")


    # players are allocated cards
    print("\nallocating 10 cards to players\n")
    time.sleep(3)
    
    deck.move_cards(computer_hand,10)
    deck.move_cards(human_hand,10)

    ## opening card identified
    print(f"\nThe card opening the game is {deck.last_card()}, card no {deck.last_card().card_no()}")
    time.sleep(3)



    # COMPUTER PLAYS

    #display players cards
    print(f"_____________________\n{computer_hand.label} \n***************\n{computer_hand}\n_____________________")

    #player plays, establish the right cards first
    last_card = deck.last_card()
    cards_next = next_cards(last_card)
    cards_right = right_cards(computer_hand.cards,cards_next)



    if len(cards_right) != 0:
        card_played = random.choice(cards_right)
        print("computer plays", card_played )
        computer_hand.move_card(deck,card_played)

    #if there are no right cards we lie
    else:
        print("computer has no option but to lie")
        print("computer plays")
        card_lie,card_play = bluff_card(computer_hand.cards,cards_next,auto_lie=False)
        print("card lied with:", card_lie)
        print("card played with:",card_play)

        #card played is moved from the hand to the deck
        computer_hand.move_card(deck,card_play)

    


if __name__ == "__main__":
    main()