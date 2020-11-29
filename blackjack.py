import random

class Card(object):
    def __init__(self,suit, val):
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
                self.card.append()
                print('{} of {}'.format(b,i)
    def show(self):
        for c in self.cards:
                      c.show()

    def shuffle(self):
            for i in range(len(self.cards)-1,0,-1):
                      rand = random.randint(0,i)
                      self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
            return self.cards.pop()


class Player(object):
        def __init__(self):
                      self.hand = []

        def draw(self, deck):
                      self.hand.append(deck.drawCard())

        def showHand(self):
                      for card in self.hand:
                      card.show()
                      
deck = Deck()
deck.shuffle()


player1 = Player('oscar')
player1.draw(deck).drawCard(deck)
player.showHand()
                      
