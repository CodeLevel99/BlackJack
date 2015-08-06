from deck import *
import random

class Hand:
    def __init__(self, size, owner):
        self.size = 0
        self.owner = owner
        self.cards = {}
    def get(self, card):
        self.size = self.size + 1
        self.cards[self.size] = card
    def show_hand(self):
        for x in range (1, self.size+1):
            return (self.cards[x])

def deal(target):
    draw = deck[random.randrange (1, 53, 1)]
    target.get(draw)
    return draw

def name(card):
   if int(card/100) == 1:
       suit = "Sp"
   elif int(card/100) == 2:
       suit = "Cb"
   elif int(card/100) == 3:
       suit = "Dm"
   else:
       suit = "Ht"

   if card%100 == 1:
       value = "Ace"
   elif card%100 == 11:
       value = "Jack"
   elif card%100 == 12:
       value = "Queen"
   elif card%100 == 13:
       value = "King"
   else:
       value = str(card%100)
   return  suit + value
