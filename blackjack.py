import random

class Card():
    def __init__(self, rank, suit, value):
        self.rank = rank
        self.suit = suit
        self.value = value
    
    def __str__(self):
        return f'{self.rank} {self.suit} (+{self.value})'

class Deck():
    def __init__(self):
        self.cards = []
        self.create_deck()
        self.shuffle_deck()
        
    def __str__(self):
        return f'{self.cards}'

    def create_deck(self):
        RANKS_VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': [1, 11]}
        SUITS = ['♣️', '♦️', '♥️', '♠️']

        for suit in SUITS:
            for key, value in RANKS_VALUES.items():
                card = Card(key, suit, value)
                self.cards.append(card)
        
    def shuffle_deck(self):
        return random.shuffle(self.cards) 

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
    # Create a deck
    deck = Deck()
    
    for card in deck.cards:
        print(card)
    
if __name__ == "__main__":
    play_game()
