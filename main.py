

class Card():
    "Models 52 cards in a game; 13 ranks and 4 suits"

    #define class attributes

    # suits ranked in ascending order
    suit_names = ["Clubs","Diamond", "Hearts", "Spades" ]

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
        for suit in range(0,4):
            #range starts from 1 because None is not a card
            for rank in range(1,14):
                card = Card(suit,rank)
                self.cards.append(card)

    def __str__(self) -> str:
        #convert the list of card objects to a list of string names then list to a string
        cards = []
        for card in self.cards:
            cards.append(str(card))

        return ",".join(cards)






if __name__ == "__main__":

    deck = Deck()

    print(deck)

    card1 = Card(0,3)
    card2 = Card(3,6)

    ans = card1 == card1
    print(card1)
    print(card2)
    print(ans)