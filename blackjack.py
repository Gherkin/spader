import random

class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val

    def show(self):
        print('{} of {}'.format(self.val,self.suit))


class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for i in ['spades','clubs','diamonds','hearts']:
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

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()

    def placeCard(self):
        return self.hand.pop

deck = Deck()
deck.shuffle()


player1 = Player('oscar')
for i in range(1,14):
    player1.draw(deck)

player1.showHand()
print('------------')
#deck.show()
