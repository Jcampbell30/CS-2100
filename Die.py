#@Author: Jared Campbell
#Date: 06/15/22
#This class represents Chevalier De Mere's Dice Probability Problem
import random
class Die:

    def __init__(self):
        self = self
    
    def diceRoll(self):
        throw = random.randint(1,6) 
        return throw
    
    def doubleSix(self,other):
        num = 0
        count = 0
        while count < 24:
            if self.diceRoll() + other.diceRoll() == 12:
                num = 1
            count+=1
        return num    
      
def main():
    dice1 = Die()
    dice2 = Die()
    count = 0
    doubleSix = 0
    while count < 10000:
        doubleSix += (dice1.doubleSix(dice2))
        count +=1
    
    probability = (doubleSix/count)
    print("The probability of rolling double sixes is: ", "% " + str(probability))


main()
        