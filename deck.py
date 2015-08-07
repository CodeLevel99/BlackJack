deck = {}
def fresh_deck():    
    deck = {}
    #Spades = 100
    #Clubs = 200
    #Diamonds = 300
    #Hearts = 400
    for x in range (1, 53):
        if x<=13:
            deck[x] = 100 +  x
        if x>13 and x<=26:
            deck[x] = 200 + x - 13
        if x>26 and x<=39:
            deck[x] = 300 +  x - 26
        if x>39:
            deck[x] = 400 + x - 39


