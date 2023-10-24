import random
import time 
from threading import Thread
from itertools import islice

tap = 0
score = 0
number_of_cards = 4


 #Timer func
def check():
            time.sleep(5)
            if tap < 0:
                return
            
            print("Too Slow")

#Generate random numbers within a given range and store in a list
def para(start, end, num):
    res = []
 
    for j in range(num):
        res.append(random.randint(start, end))

    return res
 
# Driver Code
num = 10
start = 1
end = 11
print(para(start, end, num))

Input = para(start, end, num)
 
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

while number_of_cards >= 0:
    
    #Generate a random int to be used as index
    index_x = random.randint(0,number_of_cards)
    index_y = random.randint(0,number_of_cards)

    #Retrive random number(card) from list(deck)
    x = deck[0][index_x]
    y = deck[1][index_y]

    
    print (f"Your cards: {x} and {y}")

    Thread(target = check).start()

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

    print ("     ")  

    if val == True and tap == 1:
        score+=1
    elif val == True and tap == 0:
        score-=1
    elif val == False and tap == 1:
        score-=1
    else:
        score = score

    deck[0].pop(index_x)
    deck[1].pop(index_y)

    number_of_cards -= 1

print (f"Your Score = {score}")
print (tap)