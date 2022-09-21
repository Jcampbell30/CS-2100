#Author: Jared Campbell
#Purpose: Guessing Game
#Date: September 21, 2022
from random import randint

num = 0
value = randint(1,20)
guess = int(input("I'm thinking of a number between 1 and 20, you have 3 tries: "))
num+=1
while(num < 3):
    if guess!= value:
        if guess > value:
            guess = int(input("wrong, go lower: "))
            num+=1
        else:
            guess = int(input("wrong, go higher: "))
            num+=1
    elif (guess==value):
        print("good job!")
        break

if(num == 3 and guess==value):
    print("good job!, got it on the last try")
    print("the number was",value)
    
        
if guess!= value:
    print("too many tries, the number I was thinking of was:", value)

