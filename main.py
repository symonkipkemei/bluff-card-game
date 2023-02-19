import random
import time





def card_name(card_no):
    suit = int(card_no[0])
    rank = int(card_no[1:])
    return (suit,rank)

class Card():
    "Models 52 cards in a game; 13 ranks and 4 suits"

    #define class attributes

    # suits ranked in ascending order
    suit_names = ["None","Clubs","Diamond", "Hearts", "Spades" ]

    #ranks in ascending order
    # why 2,3...are strings

    # there is card with rank 'none" we are doing this in order to allow ranks to start from index, we can avoid this by using a dictionary
    rank_names = ["None","Ace",2, 3,4,5,6,7,8,9,10,"Jack","Queen","King"]


    # define instance varibles
    def __init__(self,suit = 0,rank = 2) -> None:
        """Create an instance object
           defaults to rank = 2, suit = 0

        Args:
        
            rank (int): card rank
            
        """
        self.rank = rank
        self.suit = suit

    def __str__(self) -> str:
        return f"{Card.rank_names[self.rank]} of {Card.suit_names[self.suit]}"

    def card_no(self)-> str:
        """Each card is identified by a unique number

        Returns:
            str: Card no
        """
        
        card_no = str(str(self.suit) + str(self.rank))
        return card_no



    def __lt__(self,other):
        # check is self is less than other, suits overides ranks in strength
        if self.suit < other.suit:
            return True
        elif self.suit > other.suit:
            return False
        #check ranks if suit is the same
        else:
            if self.rank < other.rank:
                return True
            else:
                return False


class Deck:
    " cards that make up the deck"

    def __init__(self) -> None:
        self.cards = []
        #populate list with cards ( note that cards are objects)
        for suit in range(1,5):
            #range starts from 1 - 13 because None is not a card
            for rank in range(1,14):
                card = Card(suit,rank)
                self.cards.append(card)

    def __str__(self) -> str:
        #convert the list of card objects to a list of string names then list to a string to display to user
        cards = []
        for card in self.cards:
            cards.append(str(card))

        return "\n".join(cards)
    #veneer methods

    def pop_card(self, i= -1):
        """_summary_

        Args:
            i (int, optional): index of card to be popped. Defaults to -1.
        """
        return self.cards.pop(i)

    def add_card(self,card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    # a serious method

    def sort_cards(self):
        cards_dict = {}
        for card in self.cards:
            #create a key that uniquely identifies each card ( combines suit and rank)
            key = int(str(card.suit) + str(card.rank))
            cards_dict[key] = card

        #sort dictionary
        sorted_cards = sorted(cards_dict.items(), key=lambda t : t[0])

        # revert the list of cards only
        self.cards = [cards[1] for cards in sorted_cards]

    def sort_cards1(self):
        self.cards.sort()

    def move_cards(self,hand,num:int):
        """cards changes location from the deck to the hands

        Args:
            hand (_type_): type of hand
            num (int): the number of hands moving
        """
        
        for i in range(num):
            hand.add_card(self.pop_card())
            
        
    
    def last_card(self):
        "establishes the last card"
        return self.cards[-1]

    def remove_card(self,card):
        "removes a specific card from the deck"
        return self.cards.remove(card)



class ComputerHand(Deck):
    "a hand playing cards"

    def __init__(self,label) -> None:
        self.cards = []
        self.label = label

    def next_move(self,other):
        #determine the last card no
        last_card = other.last_card()
        #concatenate the suit and rank
        last_card_no = last_card.card_no()
        
        #search if the next card is within your deck
        next_suit = last_card_no[0]
        next_rank = int(last_card_no[1:]) + 1
        next_card_no = next_suit + str(next_rank)
    
   

        #create a dictionary that maps the key and the card as the value
        key_card = {}
        for card in self.cards:
            key_card[card.card_no()] = card
        
        if (next_card_no) in key_card.keys():
            next_card = key_card[next_card_no]

            print(f"{self.label} plays {next_card}")

            #cards moved from the computer to the deck
            self.remove_card(next_card)
            other.add_card(next_card)


            card_choice = next_card
          
        #check if there is any card of different suit but same rank within your hand
        
        elif next_card_no[1:] in [card[1:] for card in key_card.keys()]:

            suit_option = { card[1:]:card[0] for card in key_card.keys()}
            rank = next_card_no[1:]
            suit = suit_option[rank]
            next_card = Card(rank,suit)

            print(f"{self.label} plays {next_card}")

            #cards moved from the computer to the deck
            self.remove_card(next_card)
            other.add_card(next_card)

            card_choice = next_card
        
        else:
            #if the right card is not available, the computer chooses between 

            #computer intuitively chooses between lying and picking
            #it should be able to lie more

            user_choice = ["pick", "lie","lie"]
            choice = random.choice(user_choice)
            
            if choice == user_choice[0]:
                print(f"{self.label} picks the next card from the deck")
                #cards moved from the deck to the user
                other.move_cards(self,1)
                card_choice = None

            else :
                #randomly select a card to lie with
                choice = random.choice(self.cards)
                #lie
                next_card_suit, next_card_rank = card_name(next_card_no)
                next_card = Card(next_card_suit,next_card_rank)
                print("computer lied")

                print(f"{self.label} plays {next_card}")

                #cards moved from the computer to the deck
                self.remove_card(choice)
                other.add_card(choice)

                card_choice = choice

        #state the number of cards remaining
        print(f"\n{self.label} cards remaining are {len(self.cards)}")
        print(f"Deck cards remaining are {len(other.cards)}")

        return card_choice


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

        


def main():
        #objects are identified
    deck = Deck()

    print("WELCOME TO THE BLUFF GAME \nIf you are not cheating you are not trying enough\nEnjoy!\n")


    print("Cards are shuffled")
    deck.shuffle()
    time.sleep(10)
    print("\nshuffling is complete\n")
    

    # playing hands are identified
    username = "symon"
    computer_hand = ComputerHand("computer")


    # players are allocated cards
    print("allocating 10 cards to players")
    
    deck.move_cards(computer_hand,10)

    time.sleep(10)


    print(f"\nThe card opening the game is {deck.last_card()}, card no {deck.last_card().card_no()}")

  


    print(f"The current player is {computer_hand.label}")
    #display players cards
    print(f"_____________________\nComputers hand \n***************\n{computer_hand}\n_____________________")

    #player plays
    card_choice = computer_hand.next_move(deck)

    # call bluff
    ans = bluff()

    if ans is True and not None:
        # check oppoonents card
        print(f"last_card:{deck.last_card()}")
        print(f"card played:{card_choice}")

        if card_choice == deck.last_card():
            print("It is not a bluff, you got it wrong!")
        else:
            print("Its a bluff!")
        


        # check if the computer lied




if __name__ == "__main__":

    main()

    





 
