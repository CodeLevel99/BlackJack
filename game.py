from hand import *
from deck import *
from ai import *
import sys

#welcome message

print ("*WELCOME TO BLACKJACK*")

#1 - player, player vs ai

player = Hand(0, "player")
ai = aihand(0, "ai")

#deals two cards to player

print("You received a: " + name(deal(player)))
print("You received a: " + name(deal(player)))

#deals two cards to ai

deal(ai)
deal(ai)

#hit or stay? 

while True:
    cardsum = handvalue(player)
    print("Your cards sum up to: " + str(handvalue(player)))
    if cardsum > 21:
        print ("You're Busted!")
        break
        sys.exit(0)
    else:
        print("Would you like another card??")
        hit = input("Type in 'hit' for another card or 'stay' if you are satisfied with your current hand.")
        if hit == "stay":
            break
        elif hit == "hit":
            print("You received a: " + name(deal(player)))
#aiya

ai.choose()

#WHO WINS?????

def whowins():
    playerDiff = 21 - handvalue(player)
    aiDiff = 21 - handvalue(ai)

    if playerDiff < aiDiff:
        print ("gratz")
    elif aiDiff > playerDiff:
        print ("lol")


whowins()




          
      
