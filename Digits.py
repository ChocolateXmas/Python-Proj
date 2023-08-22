##################################
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##
## Created by: Alex Beigel      ##
## Date: 14.03.23               ##
## Program: Digits.py           ##
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##
##################################

# Digits.py
# This function gets a number (num), and prints a " Z " Shaped like from the digits of the given number.
def Digits(num):
    newNum = str(num)
    print(newNum[3] + " " + newNum[2] + " " + newNum[1] + " " + newNum[0])
    print("    " + newNum[0])
    print("  " + newNum[1])
    print(" " + newNum[2])
    print(newNum[3])
    print(newNum[0] + " " + newNum[1] + " " + newNum[2] + " " + newNum[3])

def main():
    X = int(input("> Please enter a number: "))
    Digits(X)

main()

