##################################
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##
## Created by: Alex Beigel      ##
## Date: 14.03.23               ##
## Program: DecSeries.py        ##
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##
##################################

# DecSeries.py #
# ######################### #
# Inputs 10 numbers, Algorithm finds the longest series of decreasing number in a row, simple as that
# GOAL - DO NOT use Max Function or List obj

# Function - gets a number and persists to enter only numbers with no strings
def checkNum(num):
    x = num
    while not checkFloat(x):
        x = input("> Silly, Enter an integer Number, no strings included ;) -> _")
    return float(x)
### END checkNum ###

def checkFloat(num):
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
### END CheckNum1 ###

def main():
    # To count series of decreasing numbers, count will use as a temporary value holder, biggest_count will hold the
    # "largest count of Decreasing Numbers in a row" value.
    count, biggest_count = 0, 0
    last_num = x = checkNum(input("> Enter number: "))
    series = "[ "

    for i in range(1, 10):
        x = input("> Enter number: ")
        x = checkNum(x) # Just to check if int
        if last_num > x:
            count += 1
            # Some Cool Concatenation
            series += "\033[1;4m" + str(last_num) + "\033[0m"
            if biggest_count < count:
                biggest_count = count
        elif last_num <= x:
            count = 0
            # Some Cool Concatenation
            series += str(last_num)
        if i != 9:
            series += ", "
            last_num = x
    ### END FOR ###
    if last_num > x:
        series += (", \033[1;4m" + str(x) + "\033[0m ]")
    else:
        series += ", " + (str(x) + " ]")
    print("<- Given Series -> ", series)
    print("> Biggest Series: ", biggest_count+1) if biggest_count != 0 else print("> Biggest Series: NONE")
### END main ###

main()
