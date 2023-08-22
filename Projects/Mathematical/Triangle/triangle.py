##################################
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##
## Created by: Alex Beigel      ##
## Date: 22.04.23               ##
## Program: Triangle.py         ##
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##
##################################

# Gets a number & checks if it is a legit float number.
# Note: It can be negative
def checkFloat(num):
    newNum = str(num)
    if newNum.isspace() or newNum == "":
        return False
    if newNum.isdigit():
        return False
    # Dot_Flag -> Becomes True if encounters "." (dot) for the 1st Time
    # Digit_Flag -> Becomes True if encounters a numeric digit (zero to nine include) for the 1st Time
    dot_flag, digit_flag = False, False
    for index in range(0, len(newNum)):  ### Char of the given OBJECT ###
        print(newNum[index]) # DEBUG #
        if newNum[index].isdigit():
            digit_flag = True
        elif newNum[index] == "-":  ### Dash Count ###
            if index != 0:  # Hey! you cant put a dash inside the number, only in the FIRST INDEX !
                return False
            if index == 0 and (len(newNum) == 1):  # Check if the given object is only a dash
                return False
        elif newNum[index] == ".":  ### Dot Count ###
            if index == 0 and dot_flag == False:  # A single dot cant be before numbers ;)
                return False
            if index == len(newNum) - 1 and dot_flag == False:  # Single Dot can't be in the last index without numbers after it...
                return False
            if dot_flag is True:  # If a had been detected before then its not a float number, cant b more than one . !
                return False
            dot_flag = True  # If a single dot is identified then True
        else:
            return False
    return True
### END isFloat ###

# Gets a number & checks if it is a legit Int number.
# Continuously Will input a string that is only Int Number !
# Note: IT CAN NOT be negative
def inputInt(num):
    x = num
    # print("> Input only Integers: _ ")
    while not x.isdigit():
        x = input(">>> !!! INTEGER NUMBERS ONLY !!!, -> _")
    return int(x)
### END checkNum ###

# Hmmm... A Magic loop that will concatenate chars from a given "startIndex"-Index, "times"->Amount of times
def txtloop(txt, times, startIndex):
    tmp_st = ""
    for i in range(0, times):
        if startIndex == len(txt)-1:
            tmp_st += txt[startIndex]
            startIndex = 0
        else:
            tmp_st += txt[startIndex]
            startIndex += 1
    return tmp_st, startIndex
### END txtloop ###

### Gets a String & Height. Will represent a triangle built out of the String Chars with "Height"->Rows
def get_string_triangle(string, t_height):
    tmp_st = ""
    st = str(string)
    while t_height <= 3:
        t_height = inputInt(input("> minimum height is 3, Enter new plz: _ "))
    h_spacer = int(t_height)
    slicer_index = 0
    s_toPrint = "\n"
    level = 1
    while level != t_height+1:
        h_spacer -= 1
        # 1st level of triangle
        if level == 1:
            s_toPrint += " " * h_spacer + "*" + "\n"
        # End
        elif level == t_height:
            s_toPrint += "*" * ((t_height * 2) - 1) + "\n"
        else:
            tmp_st, slicer_index = txtloop(st, ((2*level)-3), slicer_index)
            s_toPrint += " " * h_spacer + "*" + tmp_st + "*" + "\n"
        level += 1
        # ( Level = x ) : w/o(*)Char -->  (2x-1) - 2 = 2x - 3
        # x = (x-1) + x = 2x - 1 --> (2x-1) - 2
        # 1 = (1-1) + 1 = 1 First line dont!
        # 2 = (2-1) + 2 = 3 : (*)Char -> 3-2 = 1
        # 3 =     = 5 : (*)Char -> 5-2 = 3
    # print(">S2P: ", s_toPrint)
    return s_toPrint
### END get_string_triangle ###

def main():
    str = input("> Plz Enter a String ('stop' to END) : {_ ")
    while str != "stop":
        tri = get_string_triangle(
            str,
            inputInt(input("> Plz Enter triangle's height: "))
        )
        print(tri)
        str = input("> Plz Enter a String ('stop' to END) : {_ ")
### END Main ###

main()