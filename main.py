import random
import time
from itertools import islice

#Array Variables /Adjustabel/
num = 20
start_num = 1
end_num = 67

start_game = True

#Generate random numbers within a given range and store in a list
def para(start_num, end_num, num):
    res = []
 
    for j in range(num):
        res.append(random.randint(start_num, end_num))

    return res

#print(para(start_num, end_num, num))

Input = para(start_num, end_num, num)
 
# list of length in which we have to split /Adjustabel/
length_to_split = [10,10] 
 
# Using islice 
Inputt = iter(Input) 
deck = [list(islice(Inputt, elem)) 
        for elem in length_to_split] 
 
# Printing Output 
#print("List after splitting", Output) 

print ("     ")    
print ("Welcome to Tens .mark1.\n**********************\n")


# Number of card per person -1 /Adjustabel/
number_of_cards = 9
tap = 0
score = 0

#Timer /Adjustabel/
max_time = 20
start_time = time.time()

print (f"You have {max_time} Seconds")
print ("1 = Yes : 2 = No\n")

while (time.time() - start_time) < max_time:
    if number_of_cards >= 0:
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
            score +=1
        elif val == True and tap == 2:
            score -=1
        elif val == False and tap == 1:
            score -=1
        elif val == False and tap == 2:
            score +=1
        else:
            score = score
        
        #Remove used values(cards) from deck
        deck[0].pop(index_x)
        deck[1].pop(index_y)

        #Reduce the numbers of cards by 1
        number_of_cards -= 1
    else:
        print (f"Your score => {score}")
        exit()

print("You are out of Time")
print(f"You got => {score} correct")