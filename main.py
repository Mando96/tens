import random
import time
from itertools import islice

#Array Variables
num = 10
start_num = 1
end_num = 11

start_game = True

#Timer Variables
running = True
seconds = 10
end = 0

#Generate random numbers within a given range and store in a list
def para(start_num, end_num, num):
    res = []
 
    for j in range(num):
        res.append(random.randint(start_num, end_num))

    return res

#print(para(start_num, end_num, num))

Input = para(start_num, end_num, num)
 
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

def game_play():
    number_of_cards = 4
    tap = 0
    score = 0

    if number_of_cards > 0:
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

    else:
        print (f"Your score => {score}")
        exit()

time_limit = 5
start_time = time.time()

while True:
    if start_game:
        game_play()
        elapsed_time = time.time() - start_time
        print(time_limit - int(elapsed_time))
        if elapsed_time > time_limit:
            print ("Game Over")
            exit()
    else:
        print("Game Over")



'''
#Timer loop
while running:
    print(seconds)
    time.sleep(1)
    seconds -=1
    if seconds <= end :
        running = False
        print(seconds)

print("Game Over")

elapsed_time = time.time() - start_time
            print(time_limit - int(elapsed_time))
            if elapsed_time > time_limit:
                print ("Game Over")
                exit ()
'''
