import random

class Card(object):
    HEARTS = 'H'
    SPADES = 'S'
    DIAMONDS = 'D'
    CLUBS = 'C'

    def __init__(self, suit, val):
        self.suit = suit
        self.val = val

    def show(self):
        print('{} of {}'.format(self.val,self.suit))

    def __str__(self):
        return '{} of {}'.format(self.val,self.suit)

    def __eq__(self, other):
        if self.suit != other.suit:
            return False

        if self.val != other.val:
            return False

        return True

    def serialize(self):
        return [self.suit, self.val]


class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for i in ['H', 'S', 'D', 'C']:
            for b in range(1,14):
                self.cards.append(Card(i,b))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
            for i in range(len(self.cards)-1,0,-1):
                rand = random.randint(0,i)
                self.cards[i], self.cards[rand] = self.cards[rand], self.cards[i]

    def drawCard(self):
        return self.cards.pop()


class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.n = 0

    def declare(self, n):
        self.n = n

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def has(self, card):
        if card in self.hand:
            return True
        return False

    def draw_n(self, deck, num):
        for _ in range(0, num):
            self.draw(deck)

    def showHand(self):
        for card in self.hand:
            card.show()

    def placeCard(self):
        return self.hand.pop

    def serialize(self):
        json = {}
        json['name'] = self.name
        json['cards'] = [x.serialize() for x in self.hand]
        return json


if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()


    player1 = Player('oscar')
    for i in range(1,14):
        player1.draw(deck)

    player1.showHand()
    print('------------')
    #deck.show()
