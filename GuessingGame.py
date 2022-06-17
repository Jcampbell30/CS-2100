
import random
def main():
    number = random.randint(1,1000)
    while True:
        try:
            guess = int(input("Try and guess a number between 1 and 1000, enter here: \n"))
            break
        except ValueError:
            print('You must type an integer value, try again: ')
            continue
    
    while guess != number:
        try:
            if guess < number:
                print("go higher")
                guess = int(input())
            elif guess > number:    
                print("go lower")
                guess = int(input())
            else:
                break
        except ValueError:
            print('You must enter an integer, a whole number: ')
            print()
            continue

    print("You got it!")
main()

