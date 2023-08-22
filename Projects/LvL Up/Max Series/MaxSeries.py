##################################
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##
## Created by: Alex Beigel      ##
## Date: 14.03.23               ##
## Program: MaxSeries.py        ##
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##
##################################

# MaxSeries.py #
# ######################### #
# Inputs a series of numbers until 0 (zero) is pressed, when it's pressed the game stops.
# Prints the Average of the number series + Maximum number & its index position + Minimum number & its index position
# GOAL - DO NOT use Max Function or List obj

# Function - gets a number and persists to enter only numbers with no strings
def checkNum(num):
    x = num
    while not x.isnumeric():
        x = input("> Silly, Enter a Number, no strings included ;) -> _")
    return float(x)

def main():
    choice = "choice of input"
    avg, sum, count_index = 0, 0, 0
    max_num, max_index = None, None
    min_num, min_index = None, None
    while choice != 0:
        count_index += 1 # Started a new turn, will count it
        choice = input("> Plz Enter your desired number:")
        choice = checkNum(choice) # Just to check if its a real number
        if choice == 0:
            break
        # Check if its the first time playing, and if so than will assign a value for comparison with choice
        if max_num is None:
            max_num = choice
            max_index = count_index
        # Check if its the first time playing, and if so than will assign a value for comparison with choice
        if min_num is None:
            min_num = choice
            min_index = count_index
        # Check Maxmimum Number
        if choice > max_num:
            max_num = choice
            max_index = count_index
        # Check Minimum Number
        if choice < min_num:
            min_num = choice
            min_index = count_index
        sum += choice
    ### END WHILE ###
    print("> Average: ", sum / (count_index-1))
    print("> Max Value is: ", max_num, "in cell ", max_index)
    print("> Min Value is: ", min_num, "in cell ", min_index)

main()