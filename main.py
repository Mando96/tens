import random
from itertools import islice

tap = 0
score = 0
b = 4

#generate-random-numbers-within-a-given-range-and-store-in-a-list/
def deck(start, end, num):
    res = []
 
    for j in range(num):
        res.append(random.randint(start, end))
 
    return res
 
# Driver Code
num = 10
start = 1
end = 11
print(deck(start, end, num))

Input = deck(start, end, num)
 
# list of length in which we have to split 
length_to_split = [5,5] 
 
# Using islice 
Inputt = iter(Input) 
Output = [list(islice(Inputt, elem)) 
        for elem in length_to_split] 
 
# Printing Output 
#print("List after splitting", Output) 

print ("     ")    
print ("Welcome to Tens .mark1.\n**********************\n")

while b >= 0:
    indexx = random.randint(0,b)
    indexy = random.randint(0,b)

    x = Output[0][indexx]
    y = Output[1][indexy]

    sum = x + y
    if x > y:
        sub = x - y
    else:
        sub = y -x

    if sum % 10 == 0 or sub % 10 == 0:
        val = True
    else:
        val = False

    print (f"Your cards: {x} and {y}")
    tap = int(input("Ten? => "))
    print ("     ")  

    if val == True and tap == 1:
        score+=1
    elif val == True and tap == 0:
        score-=1
    elif val == False and tap == 1:
        score-=1
    else:
        score = score

    Output[0].pop(indexx)
    Output[1].pop(indexy)

    b -= 1

    #print (b)
    
#print (f"sum = {sum} and sub = {sub}")
#print (f"Is this a multiple of 10? {val}")

print (f"Your Score = {score}")