import random

class Participant:
    def __init__(self):
        self.cards = []
        self.hand_value = 0
        
    def get_card(self, cards):
        card = random.choice(cards)
        self.cards.append(card)
        cards.remove(card)

    def calc_hand_value(self):
        hand_value = 0
        num_of_aces = 0
        for card in self.cards:
            if card.value == 'A':
                num_of_aces = num_of_aces + 1
            elif card.value in ['J', 'Q', 'K']:
                hand_value = hand_value + 10
            else:
                hand_value = hand_value + card.value
        if num_of_aces == 1:
            if hand_value <= 10:
                hand_value = hand_value + 11
            else:
                hand_value = hand_value + 1
        elif num_of_aces == 2:
            if hand_value <= 9:
                hand_value = hand_value + (11 + 1)
            else:
                hand_value = hand_value + (num_of_aces * 1)
        elif num_of_aces == 3:
            if hand_value <= 8:
                hand_value = hand_value + (11 + 1 + 1)
            else:
                hand_value = hand_value + (num_of_aces * 1)
        elif num_of_aces == 4:
            if hand_value <= 7:
                hand_value = hand_value + (11 + 1 + 1 + 1)
            else:
                hand_value = hand_value + (num_of_aces * 1)
        return hand_value

class Player(Participant):
    def __init__(self, number):
        self.number = number
        self.bet_amount = self.get_bet_amount()
        super().__init__()
        
    def get_bet_amount(self):
        self.bet_amount = float(input(f'{self.__class__.__name__}{self.number}, please enter you\' bet amount: '))
        
    def __repr__(self):
        return f'{self.__class__.__name__}{self.number} has cards: {self.cards}'
    
class Dealer(Participant):
    def print_first_hand(self):
        return f'{self.__class__.__name__} has cards: {self.cards[0]}, hidden card'
    
    def __repr__(self):
        return f'{self.__class__.__name__} has cards: {self.cards}'
    
class Card:
    def __init__(self, symbol, value):
        self.symbol = symbol
        self.value = value
    
    def __repr__(self):
        return f'{self.symbol}: {self.value}'

def create_cards():
    cards = []
    for symbol in ('Diamond', 'Heart', 'Cube', 'Spde'):
        for value in [i for i in range(2, 11)] + ['J', 'Q', 'K', 'A']:
            cards.append(Card(symbol, value))
    return cards

def create_players():
    num_of_players = int(input('enter number of players: '))
    players = []
    for i in range(num_of_players):
        players.append(Player(i + 1))
    return players
    
def give_initial_cards(participants, cards):
    for i in range(1,3):
        for participant in participants:
            participant.get_card(cards)
            if (i == 2) & (participant.__class__.__name__ == 'Dealer'):
                print(participant.print_first_hand())
            else:
                print(participant)

def get_action():
    action = str(input('enter you\'re next action'))
    return action

def make_decision(action, participant):
    while action != 'satnd':
        if action == 'hit':
            # do hit function
            action = get_actiocn()
            continue
        elif action == 'double':
            #do double function
            action = get_actiocn()
            continue
        else:
            # would be split action
            pass

def hit(participant, cards):
    participant.get_cards(cards)

def double(participant):
    participant.bet_amount = 2 * (participant.bet_amount)
    # do hit  function

def play_game():
    cards = create_cards()
    
    players = create_players()
    
    dealer = Dealer()
    
    participants = [player for player in players] + [dealer]
    print(participants)
    
    give_initial_cards(participants, cards)

play_game()