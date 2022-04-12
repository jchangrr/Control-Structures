print("I'm thinking of a number between 1 and 10!")
import random
num = random.randint(1, 10)
guess1 = int(input("What's your guess? "))
if guess1 == num:
    print("You got it!")
    print("The secret number was ", num, end=".", sep="")
    print()
    print("It took you 1 try to guess the number.")
else:
    if guess1 < num:
        print("Too low, try again.")
    if guess1 > num:
        print("Too high, try again.")
    guess2 = int(input("What's your guess? "))
    if guess2 == num:
        print("You got it!")
        print("The secret number was ", num, end=".", sep="")
        print()
        print("It took you 2 tries to guess the number.")
    else:
        if guess2< num:
            print("Too low, try again.")
        if guess2> num:
            print("Too high, try again.")
        guess3 = int(input("What's your guess? "))
        if guess3 == num:
            print("You got it!")
            print("The secret number was ", num, end=".", sep="")
            print()
            print("It took you 3 tries to guess the number.")
        else:
            print("The secret number was ", num, end=".", sep="")
            print()
            print("You didn't guess the number.")
