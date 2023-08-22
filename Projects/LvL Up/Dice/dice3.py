##################################
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##
## Created by: Alex Beigel      ##
## Date: 14.03.23               ##
## Program: Dice3.py            ##
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##
##################################

# Dice3.py     #
# ######################### #
# Inputs "n" as "Amount Of Guesses"
# Inputs ^k^ as ^(k)-Amount of guesses out of (n)-Amount of games^ objects
# GOAL - To WIN -> Guess (k) out of (n) times where all the dice rolled to the same number
# ----------------------------------------------------------------------------------------#
import random


# ----------------------------------------------------------------------------------------#
# Function - gets a number and persists to enter only numbers with no strings
def checkInt(num):
    x = num
    while not x.isdigit():
        x = input("> Silly, Enter an integer Number, no strings included ;) -> _")
    return int(x)


def main():
    n = checkInt(input("> Plz Enter N: "))
    k = checkInt(input("> Plz Enter K: "))
    count = 0
    success = False
    for i in range(1, n + 1):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        dice3 = random.randint(1, 6)
        print(dice1, ", ", dice2, ", ", dice3)
        if dice1 == dice2 == dice3:
            count += 1
        else:
            continue
        if count == k:
            success = True
            games_count = i
        else:
            continue

    if success:
        print("> Reached ", k, " equal series after ", games_count, " games.")
    elif count != 0:
        print("> FAILURE! But at least there are ", count, "equal series out of ", k, "guesses.")
    else:
        print("> FAILURE!!! no guesses at all :(")


main()
