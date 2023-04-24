import random
import time

def abstract_card_suit_rank(card_no:str) -> tuple:
    """Abstract the card suit and rank when given the card no

    Args:
        card_no (str): The unique identity of each card

    Returns:
        tuple: suit, rank
    """
    
    suit = int(card_no[0])
    rank = int(card_no[1:])

    data  = (suit, rank)
    return data


class Card():
    "Models 52 cards in a game; 13 ranks and 4 suits"

    #define class attributes

    # suits ranked in ascending order, none so that cards starts at index 1
    suit_names = ["None","Clubs","Diamond", "Hearts", "Spades" ]

    #ranks in ascending order
    # why 2,3...are strings

    # there is card with rank 'none" we are doing this in order to allow ranks to start from index 1, we can avoid this by using a dictionary
    rank_names = ["None","Ace",2, 3,4,5,6,7,8,9,10,"Jack","Queen","King"]

    # define instance varibles
    def __init__(self,suit = 1,rank = 2) -> None:
        """
        Create an instance object
    
        Args:
            suit (int, optional): suit of the card. Defaults to 1.
            rank (int, optional): rank of th card. Defaults to 2.
        """
        
        self.rank = int(rank)
        self.suit = int(suit)

    def __str__(self) -> str:
        """Abstract the name of the card from the class , and the suit and rank entries

        Returns:
            str: the card name
        """
        return f"{Card.rank_names[self.rank]} of {Card.suit_names[self.suit]}"

    def card_no(self)-> str:
        """Each card is identified by a unique number,
        the unique number is a concatetation of the suit and rank 

        Returns:
            str: Card no
        """
        card_no = str(str(self.suit) + str(self.rank))
        return card_no


    def __lt__(self,other) -> bool:
        """A comparison of who is greater, less than or equal to

        Args:
            other (_type_): card object

        Returns:
            bool: True or False
        """

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
        """Instantiate a deck of 52 cards
        """
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
            #converting the objects to strings before storing them to a list
            cards.append(str(card))

        return "\n".join(cards)
    #veneer methods

    def pop_card(self, i= -1):
        """Remove a card

        Args:
            i (int, optional): index of card to be popped. Defaults to -1.
        """
        return self.cards.pop(i)
    
    def remove_card(self,card):
        "removes a specific card from the deck"
        return self.cards.remove(card)
    
    def insert_card_at_beginning(self,card):
        "Insert a specific card to the first index"
        return self.cards.insert(0,card)


    def add_card(self,card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort_cards(self):
        self.cards.sort()

    def last_card(self) -> Card:
        """establishes the last card

        Returns:
            Card: last card in the deck
        """
        
        return self.cards[-1]



    def move_cards(self,other,num:int):
        """cards changes location from the deck to the hands, the last cards are removed
        Args:
            hand (_type_): type of hand
            num (int): the number of cards changing hands
        """
        for i in range(num):
            other.add_card(self.pop_card())

    def move_card(self,other,card):
        """One specific card is changing hands
        the card is moved to the first index of the next hand from the current self list

        Args:
            card_no (_type_): _description_
        """

        # remove card from the self list

        self.remove_card(card)

        # place same card in the other list

        other.insert_card_at_beginning(card)
 
            
        


  

    

class Hand(Deck):
    """instantiate the hand of the player, inherites from the class Deck"""
    def __init__(self, label_name) -> None:
        """ cards are empty at the commencment"""
        self.cards = []
        self.label = label_name
    

def next_cards(last_card:Card) -> list:
        """Establish the next possible cards to be played , based on the last card on the deck

        Returns:
            list: possible next cards
        """
        
        #determine the last card no on the deck
        last_card_no = last_card.card_no()

        # the last rank and suit
        last_suit, last_rank = abstract_card_suit_rank(last_card_no)
    
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
    
def right_cards(cards_in_hand:list, possible_cards:list) -> list:
    """Check if possible cards is in cards in hand

    Args:
        cards_in_hand (list): cards in hand
        possible_cards (list): possible cards to be played in the next move

    Returns:
        list: The corrrect cards in the nad
    """

    correct_cards = []

    #loop through the  cards in hand, checking if the card is in possible cards

    for card_hand in cards_in_hand:
        for card_possible in possible_cards:
            if int(card_hand.card_no()) == int(card_possible.card_no()):
                correct_cards.append(card_hand)

    return correct_cards

    
def bluff_card(cards_in_hand:list,possible_cards:list,auto_lie = True) -> tuple:
    """Selects a card to lie with and card to play from a collections of cards/options respectively

    Args:
        cards_in_hand (list): The cards in the players hand
        possible_cards (list): The possible correct cards based on the last card played, that the player can possibly lie with
        auto_lie (bool, optional): Autoselect card_lie and card_play. Defaults to True.

    Returns:
        tuple: card_lie, card_play
    """

    if auto_lie:
        card_lie = random.choice(possible_cards)
        card_play = random.choice(cards_in_hand)
    else:
        #CARD LIE
        #_______________________________
        #est card map
        card_map = {}
        # display cards to user
        for index, card in enumerate(possible_cards):
            print(f"{index}:{card}")
            card_map[index] = card

        #user to select the card_lie
        card_lie_index = int(input("\nSelect the card to lie with"))
        card_lie = card_map[card_lie_index]

        #CARD PLAY
        #_______________________________
        #est card map
        card_map = {}
        # display cards to user
        for index, card in enumerate(cards_in_hand):
            print(f"{index}:{card}")
            card_map[index] = card

        #user to select the card_lie
        card_play_index = int(input("\nSelect the card to play with"))
        card_play = card_map[card_play_index]

    return (card_lie, card_play)
        

def call_bluff(autobluff= True)-> bool:
    """Call Bluff

    Args:
        autobluff (bool, optional):auto call bluff. Defaults to True.

    Returns:
        bool: Return True if call bluff

    """

    if autobluff:
        choices = [False, True]
        choice = random.choice[choices]
    else:
        print("Call bluff")
        print("****************")
        print("\n 1. Yes 2.No")
        print("****************")
        user_choice = int(input("option: "))

        if user_choice == 1:
            choice = True
        elif user_choice == 2:
            choice = False
        else:
            print("Wrong choice")

    return choice


def evaluate_bluff():
    pass


if __name__ == "__main__":
    pass