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


class Player():
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.hand = []
    
    def __str__(self):
        return f'{self.name}'

    def check_hand_value():
        pass

    def deal_cards(self, players):
        pass

    def hit(self, deck):
        self.hand = deck.cards.pop(0)

def play_game():
    # Create a deck
    deck = Deck()
    
    # Create players
    players = []
    dealer = Player('Dealer', 'dealer')
    player_user = Player(input('Enter player name: '), 'player')
    players.extend([dealer, player_user])
    print(f'Player 1, {player_user}, will be playing against the {dealer}.')
    print(f'Let\'s play Blackjack, {player_user}!')
    player_user.hit(deck)
    print(f'{player_user}\'s hand: {player_user.hand}')


    
if __name__ == "__main__":
    play_game()
