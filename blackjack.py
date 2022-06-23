class Card():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = None
    
    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck():
    def __init__(self):
        self.cards = []
        self.create_deck()
        
    def __str__(self):
        return f'{self.cards}'

    def create_deck(self):
        RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]
        VALUES = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, [1, 11]]
        
        for suit in SUITS:
            for rank in RANKS:
                card = Card(rank, suit)
                self.cards.append(card)
        
    def suffle():
        pass
    def deal():
        pass
    def draw():
        pass

class Player():
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.hand = []
        
    def hit():
        pass

    def check_hand_value():
        pass

def play_game():
    deck = Deck()
    deck.create_deck()
    [print(card) for card in deck.cards]

if __name__ == "__main__":
    play_game()
