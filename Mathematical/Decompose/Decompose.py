##################################
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##
## Created by: Alex Beigel      ##
## Date: 12.06.23               ##
## Program: Decompose.py        ##
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##
##################################
import math


def decompose(num, div=2):
    if num < 0: # Negative Number
        return "Error Negative Number !!!"
    elif num < 2: # Positive Number, but need to check whether it bigger than the divider "2"
        return num

    if num == div:
        # Stop statement, "num" has reached to divider, so here we exit & return the last divider
        # Because every number is divisible by itself
        return str(div)
    elif num % div == 0:
        # Divisible! so divide and add the divider to the Returned String
        return decompose(num/div, div) + "*" + str(div)
    elif num % div != 0:
        # Not divisible, so increment in one to the next divider
        return decompose(num, div+1)
### END decompose() ###

# Will accept only Integers for input
def custom_int_input():
    while n := input(">Number: _"):
        # print("D")
        try:
            int(n)
            break
        except ValueError as e:
            print("> Only Integers are allowed. . .")
    return int(n)
### END custom_int_input ###

def main(option_num):
    # s = "5*2"
    #
    # print( decompose(98.5) )
    # num = int( input(">Number: _") )
    while option_num != 0:
        print( decompose(option_num) )
        option_num = custom_int_input()
    # END while #
### END main() ###

if __name__ == "__main__":
    main(custom_int_input())