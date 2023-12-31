#Random_Number_Game
import random
random_integer = random.randint(0,100)
attempts = 0
while True:
    A1 = int(input("Guess Number: "))
    attempts += 1
    if A1 > random_integer:
        print("Enter A Smaller Number")
    elif A1 < random_integer:
        print("Enter A Larger Number")
    else:
        print("Well Done \nYou Guessed It")
        print(f"You Took : {attempts} Attempts")
        break