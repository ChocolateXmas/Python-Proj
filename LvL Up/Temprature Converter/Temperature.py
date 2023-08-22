##################################
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##
## Created by: Alex Beigel      ##
## Date: 14.03.23               ##
## Program: Temperature.py      ##
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##
##################################

# Temperature.py #
# ########################### #
# ----------------------------------------------------------------------------------------#
import random
# ----------------------------------------------------------------------------------------#
# Function - gets a number and persists to enter only numbers that they're Temperatures
def checkTemperature(num):
    x = str(num)
    while isFloat(x) == False:
        x = input("> Silly, Enter ONLY Temperature Numbers, no strings included ;D -> _")
    return float(x)
### END checkTemperature ###

### Float number ###
# A float number can have:
# 1) Digits Of Course...
# 2) "-" (Negative Symbol) Can be shown only Once in the first cell, If NOT then it isn't a float number
# 3) "." (Dot Symbol) Can be shown only once BUT Cannot be in the first cell && One cell after the dot must be a digit!
### ############ ###
def isFloat(num):
    newNum = str(num)
    if newNum.isspace() or newNum == "":
        return False
    # Dot_Flag -> Becomes True if encounters "." (dot) for the 1st Time
    # Digit_Flag -> Becomes True if encounters a numeric digit (zero to nine include) for the 1st Time
    dot_flag, digit_flag = False, False
    for index in range(0, len(newNum)):  ### Char of the given OBJECT ###
        # print(newNum[index]) # DEBUG #
        if newNum[index].isdigit():
            digit_flag = True
        elif newNum[index] == "-":  ### Dash Count ###
            if index != 0:  # Hey! you cant put a dash inside the number, only in the FIRST INDEX !
                return False
            if index == 0 and (len(newNum) == 1):  # Check if the given object is only a dash
                return False
        elif newNum[index] == ".":  ### Dot Count ###
            if index == 0 or digit_flag == False:  # A single dot cant be before numbers ;)
                return False
            if dot_flag is True:  # If a had been detected before then its not a float number, cat be more than one . !
                return False
            if index == len(newNum) - 1:  # Single Dot can't be in the last index without numbers after it...
                return False
            dot_flag = True  # If a single dot is identified then True
        else:
            return False
    return True
### END isFloat ###

zero_kelvin = -273.15  # >>> wrong temperature #

# Function - Calculation from Fahrenheit to Celcius, Returns "Wrong Temperature" if below zero kelvin point
def fahr2celcius(F):
    calc = float( ((F - 32) * 5) / 9 )
    if F > zero_kelvin:
        return "%.2f" % calc + "°"
    return "Wrong Temperature"
### END fahr2celcius ###

# Function - gets a number and persists to enter only numbers with no strings
def checkInt(num):
    x = num
    while not x.isdigit():
        x = input(">>> !!! INTEGER NUMBERS ONLY !!!, -> _")
    return int(x)
### END checkNum ###

def main():
    F = checkTemperature( input(">>> °F: _ ") ) # Temperature in Fahrenheit
    F2C = fahr2celcius(F) # Temperature calculated into Celcius
    print("<<<", F2C, "C >>> , Type: ", type(F2C))
    # ------------------------------------------------ #
    style_choice = "@#*-+_±"
    char = style_choice[random.randint( 0, len(style_choice)-1 )]
    # ------------------------------------------------ #
    high = checkTemperature(input(">>> Higher Temp °F: _ ") )
    low = checkTemperature(input(">>> Lower Temp °F: _ ") )
    lines = checkInt(input(">>> Number of lines: _ ") )
    difference = high # Just a temporary value
    high = max(high, low)  # Higher Temp
    low = min(difference, low) # Lower Temp
    difference = (high - low) / (lines - 1) # The real calculation for this object is the multiplation of lines to show
    Table = [ ["Fahrenheit", "Celcius"] ]
    # To fill up the table with values of temperatures
    while lines != 0:
        Table.append([ str("%.2f" % high), str(fahr2celcius(high)) ])
        high -= difference
        lines -= 1
    coolString2Print = char + ' {:^18} ' + char + ' {:^18} ' + char
    print(char * 43)
    for row in Table:
        if Table.index(row) == 1:
            print(char * 43)
        print( (coolString2Print.format(*row) ) )
    print(char * 43)
### END main ###

main()