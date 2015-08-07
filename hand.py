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
            print(self.cards[x])

def deal(target):
    while True:
        draw = random.randrange (1, 53, 1)
        card = deck[draw]
        if card != 0:
            break
    target.get(card)
    deck [draw] = 0
    return card

def name(card):
   if int(card/100) == 1:
       suit = "Spade"
   elif int(card/100) == 2:
       suit = "Club"
   elif int(card/100) == 3:
       suit = "Diamond"
   else:
       suit = "Heart"

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

def check(card, target):
    if card%100 == 11 or card%100 == 12 or card%100 == 13:
        cardValue = 10
    elif card%100 == 1:
        for x in range (1, target.size+1):
            if target.cards[x]%100 == 11 or target.cards[x]%100 == 12 or target.cards[x]%100 == 13:
                cardValue = 11
                break
            else:
                cardValue = 1
    else:
        cardValue = card%100
        
    return cardValue

def handvalue(target):
    current = 0
    for x in range(1, target.size+1):
        current = current + check(target.cards[x], target)
    return current



fresh_deck()
