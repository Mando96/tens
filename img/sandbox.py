import random
import time
from itertools import islice

# getting numbers from 1 to 60
inputNumbers =range(1,61)
# saving 60 random numbers from the given range of numbers which are
# non-repeating using sample() function into deckk
deckk = random.sample(inputNumbers, 60)

# list of length in which we have to split /Adjustabel/
length_to_split = [30,30] 
 
# Using islice to divide into different decks 
Inputt = iter(deckk) 
deck = [list(islice(Inputt, elem)) 
        for elem in length_to_split] 

# Printing Output 
#print(f"{deck}") 

print ("     ")    
print ("Welcome to Tens .mark1.\n**********************\n")

# Number of card per person -1 /Adjustabel/
number_of_cards = 32
tap = 0
score = 0
pen = 0  
index_x = 0
index_y = 0

#Timer /Adjustabel/
max_time = 150
start_time = time.time()

print (f"You have {max_time} Seconds")
print ("1 = Yes : 2 = No\n")
#print (deck)

while (time.time() - start_time) < max_time and pen < 3:
    if number_of_cards >= 0:

        #Retrive number(card) from list(deck)
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
            score +=1
        elif val == True and tap == 2:
            pen +=1
        elif val == False and tap == 1:
            pen +=1
        elif val == False and tap == 2:
            score == score
        elif tap != 1 or tap != 2:
            print("Invalid response: Use 1 or 2")
        else:
            score = score
        
        # Allowing the last card played to be used in the next play.
        if index_x == index_y:
            index_x +=1
        elif index_x > index_y:
            index_y +=1
        elif index_x < index_y:
            index_x +=1

        #Reduce the numbers of cards by 1
        number_of_cards -= 1

    else:
        print (f"Your score => {score} and pen = {pen}")
        exit()

if pen >= 3:
    print("You got too many wrong anwers")
    print(f"You got => {score} correct and {pen} penalties")
else:
    print("You are out of Time")
    print(f"You got => {score} correct and {pen} penalties")