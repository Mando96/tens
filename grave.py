import random
import time
from itertools import islice

tap = 0
score = 0

number_of_cards = 4

num_quantity = 10
first_num = 1
last_num = 11

running = True
seconds = 10
end = 0





#Generate random numbers within a given range and store in a list
def para(first_num, last_num, num_quantity):
    res = []
 
    for j in range(num_quantity):
        res.append(random.randint(first_num, last_num))

    return res

print(para(first_num, last_num, num_quantity))

Input = para(first_num, last_num, num_quantity)
 
# list of length in which we have to split 
length_to_split = [5,5] 
 
# Using islice 
Inputt = iter(Input) 
deck = [list(islice(Inputt, elem)) 
        for elem in length_to_split] 
 
# Printing Output 
#print("List after splitting", Output) 

print ("     ")    
print ("Welcome to Tens .mark1.\n**********************\n")



while number_of_cards > 0:
    #Generate a random int to be used as index
    index_x = random.randint(0,number_of_cards)
    index_y = random.randint(0,number_of_cards)

    #Retrive random number(card) from list(deck)
    x = deck[0][index_x]
    y = deck[1][index_y]

    
    print (f"Your cards: {x} and {y}")

    tap = int(input("Ten? => "))

    #Add and Subtract cards 
    sum = x + y
    if x > y:
        sub = x - y
    else:
        sub = y -x

    #Validate if sum or difference is multiple of 10
    if sum % 10 == 0 or sub % 10 == 0:
        val = True
    else:
        val = False  

    #Validate if user input(tap) is correct
    if val == True and tap == 1:
        score+=1
    elif val == True and tap == 0:
        score-=1
    elif val == False and tap == 1:
        score-=1
    else:
        score = score
    
    #Remove used values(cards) from deck
    deck[0].pop(index_x)
    deck[1].pop(index_y)

    #Reduce the numbers of cards by 1
    number_of_cards -= 1

        
print (f"Your score => {score}")


##################################################

import random

#Build a deck of cards and shuffle. This will just be cards numbered 1 - 60 

def build_deck():
    card = [*range(1,61,1)]
    random.shuffle(card)

    print (card)

    return card

cards = build_deck()

# Function to split card deck into smaller list
def serve_cards(num_cards):
    drawn_cards = []

    for i in range(num_cards):
        drawn_cards.append(cards.pop(0))

    return drawn_cards

# List of players
players = []
num_players = int(input("How many players?  "))

#number of cards per players 
split = int(60 / num_players)

#serving cards to each player
for player in range(num_players):
    players.append(serve_cards(split))

player_turn = 0
play_direction = 1