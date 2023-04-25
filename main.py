import random
import time

from parameters import *





class ComputerHand(Deck):
    "a hand playing cards"

    def __init__(self,label) -> None:
        self.cards = []
        self.label = label

    def right_cards(self,other):
        #etablish the cards that are right and consistent to be the next possible cards and available in your hand
        self.right_cards = []
        for my_card in self.cards:
            for next_card in other.next_cards():
                if my_card == next_card:
                    self.right_cards.append(my_card)
        
        return self.right_cards


    def next_move(self,other):
       
        #if the right card list is empty, it means we do not have the correct card, we have to pick or lie

        if not self.right_cards:
            #computer intuitively chooses between lying and picking
            #it should be able to lie more

            user_choice = ["pick", "lie","lie"]
            choice = random.choice(user_choice)

            if choice == user_choice[0]:
                print(f"{self.label} picks the next card from the deck")

                #cards moved from the deck to the user
                other.move_cards(self,1)
                card_choice = 0
            
            else :
                #randomly select a card to play
                card_choice = random.choice(self.cards)

                # randomly selects the card (the appropiate one) to lie with,not that this is a lie
                lie_choice = random.choice(other.next_cards())
                print(f"{self.label} plays {lie_choice}")

                #cards moved from the computer to the deck
                self.remove_card(card_choice)
                other.add_card(card_choice)

                card_choice = choice

        else:
            card_choice = random.choice(self.right_cards)


        return card_choice

    def calls_bluff(self):
        options = ["y", "n"]
        user_choice = random.choice(options)

        if user_choice == str.lower("y"):
            return True
        elif user_choice == str.lower("n"):
            return False
           
 
        

class HumanHand(ComputerHand):
    def next_move(self, other):
        # display possible play options and let the user decide
        displayed_cards_1 = {}
        displayed_cards_2 = {}

        print("Correct and available cards to play")

        if self.right_cards is not None:
            for index,card in enumerate(self.right_cards,1):
                displayed_cards_1[index] = card
                print( f"{index}:{card}")
        else:
            print("[not available]")
    
    def calls_bluff(self):
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