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
        self.rank = int(rank)
        self.suit = int(suit)

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

    def sort_cards(self):
        self.cards.sort()

    def move_cards(self,hand,num:int):
        """cards changes location from the deck to the hands

        Args:
            hand (_type_): type of hand
            num (int): the number of hands moving
        """
        
        for i in range(num):
            hand.add_card(self.pop_card())


    def next_cards(self):
        """Establish the next possible cards to be played , based on the opening card on the deck

        Args:
            other (any): the deck
        """

        #determine the last card no on the deck
        last_card = self.cards[-1]
        last_card_no = last_card.card_no()

        # the last rank and suit
        last_suit = last_card_no[0]
        last_rank = last_card_no[1:]
        
        # possible_cards to be played
        possible_cards = []


        # establish the next card of the same suit
        next_suit = int(last_suit)
        next_rank = int(last_rank) + 1

        if next_rank > 13:
            next_rank = 1
            
        card = Card(next_suit,next_rank)

        possible_cards.append(card)


        # establish the next card of different suits but same rank
        next_rank = last_rank

        
        for next_suit in range(1,5):
            if next_suit != int(last_suit):
                card = Card(next_suit,next_rank)
                possible_cards.append(card)

        return possible_cards   
    
    
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

        
        print("Cards that you can lie , you've played ")
        possible_lie_cards = []
        for card in other.next_cards():
            if card not in self.cards:
                possible_lie_cards.append(card)


        for index, card in enumerate(possible_lie_cards, len(self.right_cards)):
            displayed_cards_1[index] = card
            print( f"{index}:{card}")

        print("0. Pick a card from the deck")

        userchoice = int(input("select card to play, (0) to pick a card from the deck"))
    
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

    print("WELCOME TO THE BLUFF GAME \nIf you are not cheating you are not trying enough\nEnjoy!\n")


    # cards shuffled

    print("Cards are shuffled")
    deck.shuffle()
  
    print("\nshuffling is complete\n")
    

    # playing hands are identified
    print("\nPlayers are identified\n")
    

    computer_hand = ComputerHand("computer")
    human_hand = HumanHand("Symon")

    print(computer_hand.label)
    print(human_hand.label)


    # players are allocated cards
    print("\nallocating 10 cards to players\n")
    
    deck.move_cards(computer_hand,10)
    deck.move_cards(human_hand,10)

    ## opening card identified
    
    print(f"\nThe card opening the game is {deck.last_card()}, card no {deck.last_card().card_no()}")



    # COMPUTER PLAYS

    #display players cards
    print(f"_____________________\n{computer_hand.label} \n***************\n{computer_hand}\n_____________________")

    #player plays, establish the right cards first
    computer_hand.right_cards(deck)
    card_choice = computer_hand.next_move(deck)
    last_card = deck.cards[-2]

    # the user decides to call bluff or not, if not the game conitnues

    ans = computer_hand.calls_bluff()
    bluff_outcome(last_card,card_choice,ans)
    
        
    # HUMAN PLAYS

    #display players cards
    print(f"_____________________\n{human_hand.label} \n***************\n{human_hand}\n_____________________")

    #player plays, establish the right cards first
    human_hand.right_cards(deck)
    card_choice,last_card= human_hand.next_move(deck)

    ans = human_hand.calls_bluff()
    bluff_outcome(last_card,card_choice,ans)


if __name__ == "__main__":
    main()