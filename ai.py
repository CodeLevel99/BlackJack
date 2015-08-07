from hand import *
from deck import *


class aihand:
    def __init__(self, size, owner):
        self.size = 0
        self.owner = owner
        self.cards = {}
    def get(self, card):
        self.size = self.size + 1
        self.cards[self.size] = card
    def show_hand(self):
        for x in range (1, self.size+1):
            print (self.cards[x])
    def choose(self):
        need = 21-handvalue(self)
        if need>3:
            deal(self)

bot = aihand (0, "Bro")

bot.get(101)
bot.show_hand()
bot.get(202)
bot.show_hand()
bot.choose()
bot.show_hand()

