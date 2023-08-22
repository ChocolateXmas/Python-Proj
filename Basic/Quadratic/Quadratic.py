##################################
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##
## Created by: Alex Beigel      ##
## Date: 14.03.23               ##
## Program: Quadratic.py        ##
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##
##################################

# Quadratic.py
# This Function is given 3 parameters, these 3 are the variables of a quadratic equation from the form below:
# ax² + bx + c = 0
# The Function will print if there is no solutions at all, or if there's 2 or 1 solution.
def Quad(a, b, c):
    Delta = b**2 - 4*a*c
    if Delta >= 0:
        solution1 = ( (-1)*b + (Delta)**0.5 ) / ( 2 * a )
        solution2 = ( (-1)*b - (Delta)**0.5 ) / ( 2 * a )
        if solution1 == solution2:
            print("> One Solution: " + str(solution1))
        else:
            print("> Two Solutions: ( " + str(solution1) + ", " + str(solution2) + " )")
    else:
        print("> No Solutions !")

def main():
    a = float(input("> Enter first parameter: "))
    b = float(input("> Enter second parameter: "))
    c = float(input("> Enter third parameter: "))
    print("-> { " + str(a) + "x² + " + str(b) + "x + " + str(c) + " = 0 }")
    Quad(a, b, c)

main()