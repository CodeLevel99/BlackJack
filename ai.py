import hand
import deck


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
            return (self.cards[x])
    def choose(self):
        need = 21-value
        if need<3:
            choice = "stand"
        else:
            choice = "hit"
        return choice



