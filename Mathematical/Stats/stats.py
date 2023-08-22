##################################
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##
## Created by: Alex Beigel      ##
## Date: 22.04.23               ##
## Program: Stats.py            ##
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##
##################################

### < Float number > ###
# A float number can have:
# 1) Digits Of Course...
# 2) "-" (Negative Symbol) Can be shown only Once in the first cell, If NOT then it isn't a float number
# 3) "." (Dot Symbol) Can be shown only once BUT Cannot be in the first cell && One cell after the dot must be a digit!
# Will return True if the given input is a float number, Else False
### ############ ###
def isFloat(num):
    newNum = str(num)
    if newNum.isspace() or newNum == "":
        return False
    if newNum.isdigit():
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

####### < checkIntegers > ########
## this function gets a number and checks for commas in it
## if the commas are in the *Correct Mathematical Position* then A List of their numbers will be returned
## Else --> An Empty List will be returned
##################################
def checkIntegers(line):
    new_line = str(line) # Copy of the given string
    catString = "" # A Concatenation String that will hold integer numbers only, with or w/o commas in it
    comma_count = 0 # Counter for commas --> " , "
    digit_count = 0 # Counter for digits --> 0 to 9
    Numbers = [] # List of Mathematically legit numbers, the
    ### ~-~ 'Zcount' is just for analysis: How many times this function was called :) ~-~ ###
    Zcount = 0
    pass_count = 0 ### "Mivtza Pesach" : Shows how many iterations to skip

    ### Helper Inner Function ###
    # * will restore all the inner function variables to their default values,
    # * but can change one or many values at one time while the other un-given args will reset as well.
    def startOver(new_catstring="", new_digit_count=0, new_comma_count=0):
        nonlocal Zcount, catString, digit_count, comma_count
        Zcount += 1
        catString = new_catstring
        digit_count = new_digit_count
        comma_count = new_comma_count
        # print("Called> ", Zcount, end="\n\n") ### DEBUG ###
    for i in range(0, len(new_line)):
        # print(">>> Place OF ( [", i, "] : ", new_line[i],  " )", "\n{ ", line, "}") ### DEBUG ###
        # print("{ ", line[0:i+1], "_"*(len(new_line)-i-1), "}") ### DEBUG ###
        ### LAST INDEX ###
        # Remember! ALWAYS End of range() will give len()-1
        if i == len(new_line)-1:
            if new_line[i].isdigit():
                if catString.isdigit():
                    # print("END >> CAT> ", catSt
                    catString += new_line[i]
                    Numbers.append(int(catString))
                    # print("Numbers = ", Numbers) ### DEBUG ###
                    break
                else:
                    Numbers.append(int(new_line[i]))
                    break
            else:
                if catString.isdigit():
                    # print("END >> CAT> ", catString) ### DEBUG ###
                    Numbers.append(int(catString))
                    # print("Numbers = ", Numbers) ### DEBUG ###
                    break
                else:
                    break
        ### MiVTZA PESACH ###
        if pass_count != 0:
            # print("Passed> ", pass_count) ### DEBUG ###
            pass_count -= 1
            continue
        ### <START OF ALGORITHM> ###
        else:
            # print(">>> Place OF ( [", i, "] : ", new_line[i],  " )", "\n{ ", line, "}") ### DEBUG ###
            # print("{ ", line[0:i+1], "_"*(len(new_line)-i-1), "}") ### DEBUG ###
            if new_line[i].isdigit():
                # !Fixed Mathematically --> All good continue
                if digit_count == 3 and comma_count == 1:
                    # print("B4 Slice: ", catString) ### DEBUG ###
                    # print("B3 Slice: ", catString[0:- 3]) ### DEBUG ###
                    Numbers.append( int(catString[0:len(catString) - 3]) )
                    # print("Numbers = ", Numbers) ### DEBUG ###
                    catString = catString[len(catString) - 3:len(catString)] + new_line[i]  # OVERRIDING
                    # print("A7 Slice: ", catString) ## DEBUG ###
                    digit_count = 3
                    comma_count = 0
                    # print("Comma: ", comma_count) ### DEBUG ###
                    continue
                # Has more than 4 Digits and no commas?! keep counting and digits adding ;)
                elif digit_count >= 4 and comma_count == 0:
                    catString += new_line[i] # Adding
                    digit_count += 1 # Counting
                    continue
                # ...?Well, Something has to happen, right?...
                # if the concatenated string only meets digits, just add them, NO QUESTION ASKED
                catString += new_line[i] # Adding
                digit_count += 1 #counting
                # print("CAT> ", catString)
                # print("i> ", i)
                continue
            # ##- END OF DIGIT -## #
            ########################
            ### IF IT IS A COMMA ###
            elif new_line[i] == ",":
                # If there are no digits, continue forward to next iteration
                ## Digits !found --> Not Counting anything --> Continue to Next Move ###
                if digit_count == 0:
                    continue
                comma_count += 1  # Count a Comma ya
                ### IF Continuous Count of Digits > 4 --> Comma !fixed Mathematically --> Reset all & Next Move ###
                if digit_count >= 4:
                    Numbers.append(int(catString))
                    # print("Numbers = ", Numbers) ### DEBUG ###
                    # print(">CAT: ", catString) ### DEBUG ###
                    startOver()
                    continue  # Start Count a new number
                ### Start of number check ###
                # elif 1 <= digit_count <= 3: #
                elif 1 <= digit_count <= 3:
                    # print(" 1 <= digit_count <= 3,    ->  ", digit_count)  ### DEBUG ###
                    # if len(new_line)-4 <= i+3 <= len(new_line)-1:
                    # print(">B4 Enter Ifs: ", catString) ### DEBUG ###
                    if catString[0] == "0" and digit_count == 1:
                        Numbers.append(int(catString))
                        startOver()
                        continue
                    elif i+3 > (len(new_line)-1): # Out Of Bounds
                        # print("i: ", i, new_line[i]) ### DEBUG ###
                        # print(len(new_line)) ### DEBUG ###
                        # print(len(new_line)-1) ### DEBUG ###
                        # print(i+3) ### DEBUG ###
                        Numbers.append(int(catString))
                        # print("Numbers = ", Numbers) ### DEBUG ###
                        # print(">CAT: ", catString) ### DEBUG ###
                        startOver()
                        continue
                    ## IF Comma !found b4 Digit  --> 1st Add the number, Then
                    #  --> Comma !fixed Mathematically --> Reset all & Next Move ###
                    elif i+3 <= (len(new_line)-1):  # Comma is not fixed mathematically
                        if new_line[i - 1].isdigit() \
                                and new_line[i + 1].isdigit() \
                                and new_line[i + 2].isdigit() \
                                and new_line[i + 3].isdigit():
                            # print("> A Comma Found. need to check if it's Math Legit") ### DEBUG ###
                            # print(new_line[i + 1]) ### DEBUG ###
                            # print(new_line[i + 2]) ### DEBUG ###
                            # print(new_line[i + 3]) ### DEBUG ###
                            catString += new_line[i + 1] + new_line[i + 2] + new_line[i + 3]
                            # print("HEREEEE")
                            # print(catString) ### DEBUG ###
                            digit_count = 3
                            comma_count = 1
                            pass_count = 3
                            # i = i + 3
                            continue
                        else:
                            Numbers.append(int(catString))
                            startOver()
                            continue
            # ##- END OF COMMA -## #
            ########################
            ###  IF IT IS A DOT  ###
            elif new_line[i] == ".":
                if digit_count == 0:
                    continue
                elif new_line[i+1].isdigit():
                    # We got a Float Villain here, keep and eye on him, he might be risky
                    catString += new_line[i]
                    continue
            # ##-  END OF Dot  -## #
            ########################
            ### !Digit & !Comma ###
            else:
                if catString == "":
                    continue
                else:
                    # print("b4: ", catString) ### DEBUG ###
                    print("Is Float Cat> ", catString)
                    print("Is Float > ", isFloat(catString))
                    if isFloat(catString):
                        # Numbers.append(float(catString))
                        startOver()
                        continue
                    else:
                        Numbers.append(int(catString))
                        startOver()
                        continue
                    # print("Numbers = ", Numbers) ### DEBUG ###
                    # print(">CAT: ", catString) ### DEBUG ###
                    # print(">PARGIITTTTT") ### DEBUG ###
                    # print(">CAT: ", catString) ### DEBUG ###
        # print(">>> EENNDD OF ( ", i, " : ", new_line[i], " )")### DEBUG ###
    # print("\n\n\n<<< EEEEE NnNnNnN DDDDD>>>\nNumbers = ", Numbers, "\n<~ X END X ~>\n\n\n") ### DEBUG ###
    return Numbers
### END checkIntegers ###

### Just for fun, makes some cool text and stats info for the console
def activateStats(maxvalue, maxline, minvalue, minline, sum, amount, order):
    print("################################################")
    print("## ░██████╗████████╗░█████╗░████████╗░██████╗ ##")
    print("## ██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██╔════╝ ##")
    print("## ╚█████╗░░░░██║░░░███████║░░░██║░░░╚█████╗░ ##")
    print("## ░╚═══██╗░░░██║░░░██╔══██║░░░██║░░░░╚═══██╗ ##")
    print("## ██████╔╝░░░██║░░░██║░░██║░░░██║░░░██████╔╝ ##")
    print("## ╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░╚═════╝░ ##")
    print("###*##*#########################################")
    print(">++|++|+->) Max Value is: ", maxvalue)
    print(">++|++|+->) Max @ Line: ", maxline + 1)
    print(">++|++|+->) Min Value is: ", minvalue)
    print(">++|++|+->) Min @ Line: ", minline + 1)
    print(">++|++|+->) Average: ", sum / amount )
    if order is None:
        print(">++|++|+->) Order: NOT ORDERED !!!")
    elif order:
        print(">++|++|+->) Order: Ascending ! (UP)")
    elif not order:
        print(">++|++|+->) Order: Descending ! (DOWN)")
    print("###*##*#########################################")
### END activateStats ###

def main():
    lines = None
    num_arr, tmp_arr = [], []
    max_num, min_num = None, None
    max_index, min_index = None, None
    ### Ordered = ###
    #   True    : Ascending Order
    #   False   : Descending Order
    #   None    : Not Ordered at all ( Default Value)
    Ordered = None
    sum = 0 # Sum of numbers for the Average
    ##################################
    ## "r" - Read - Default value. Opens a file for reading, error if the file does not exist
    ## "a" - Append - Opens a file for appending, creates the file if it does not exist
    ## "w" - Write - Opens a file for writing, creates the file if it does not exist
    ## "x" - Create - Creates the specified file, returns an error if the file exists
    ##################################
    try:
        file = open("numbers1.txt", "r")
        lines = file.readlines()
        file.close()
    except FileNotFoundError:
        print("> File does not exist! ")

    if lines is None:
        print("> NO LINES IN FILE!")
    else:
        print("> Lines are fine man keep going.")
        # Read every single line & check if there are Integer numbers in it, if it does - Then Activate the " Magic "
        for index in range(0, len(lines)):
            print("Line -", (index+1), "- -->", lines[index], end=f' <End of LINE -{index+1}-\n')
            tmp_arr = checkIntegers(lines[index])
            print("Numbers in this line: ", tmp_arr, "\n")
            if len(tmp_arr) != 0: # We don't want empty cells :P
                for x in range(0, len(tmp_arr)):
                    # print(tmp_arr[x])
                    # print("Added")
                    num_arr.append(tmp_arr[x])
                    # print(x, num_arr[x])
                    # Check if its the first time playing, and if so than will assign a value for comparison with choice
                    if max_num is None:
                        max_num = tmp_arr[x]
                        max_index = index
                    # Check if its the first time playing, and if so than will assign a value for comparison with choice
                    if min_num is None:
                        min_num = tmp_arr[x]
                        min_index = index
                    # Check Maximum Number
                    if tmp_arr[x] > max_num:
                        max_num = tmp_arr[x]
                        max_index = index
                    # Check Minimum Number
                    if tmp_arr[x] < min_num:
                        min_num = tmp_arr[x]
                        min_index = index
                    sum += tmp_arr[x]
                ### END FOR - tmp_arr - LOOP ###
            tmp_arr.clear()
        ### END FOR - lines - LOOP ###
        # Check the order of numbers in the list: Ascending, Descending or Not Ordered
        # --Reminder-- #
        #               True  : Ascending Order
        #   Ordered --> False : Descending Order
        #               None  : Not Ordered at all ( Default Value)
        for i in range(0, len(num_arr)):
            # Check for the 1st & 2nd index, so we can tell what order to check for the next cells
            if i == 0:
                if num_arr[i] < num_arr[i+1]:
                    # Now all the other numbers need to be in an Ascending order, If NOT --> Not Ordered
                    Ordered = True
                    continue
                elif num_arr[i] > num_arr[i+1]:
                    # Now all the other numbers need to be in a Descending order, If NOT --> Not Ordered
                    Ordered = False
                    continue
                else:
                    Ordered = None # Not ordered at all
                    break
            # As long as it's not the last index, keep checking...
            elif i != len(num_arr) - 1:
                # if Ordered is None:
                #     break
                if Ordered: # Ascending order
                    # So... Is it still ascending and keeping on this order? great, keep up
                    if num_arr[i] < num_arr[i+1]:
                        continue
                    # The order isn't cool anymore, set it to None and break the whole operation
                    else:
                        Ordered = None
                        break
                elif not Ordered: # Descending order
                    # So... Is it still descending and keeping on this order? great, keep up
                    if num_arr[i] > num_arr[i+1]:
                        continue
                    # The order isn't cool anymore, set it to None and break the whole operation
                    else:
                        Ordered = None
                        break
            ### Last Index ###
            elif i == len(num_arr) - 1:
                if Ordered: # Ascending order
                    # So... Is it still ascending and keeping on this order? great, keep up
                    if num_arr[i] > num_arr[i-1]:
                        continue
                    # The order isn't cool anymore, set it to None and break the whole operation
                    else:
                        Ordered = None
                        break
                elif not Ordered: # Descending order
                    # So... Is it still descending and keeping on this order? great, keep up
                    if num_arr[i] < num_arr[i-1]:
                        continue
                    # The order isn't cool anymore, set it to None and break the whole operation
                    else:
                        Ordered = None
                        break
        ### END FOR - num_arr - LOOP ###
        print("\n\n")
        print(num_arr)
        activateStats(max_num, max_index, min_num, min_index, sum, len(num_arr), Ordered)
### END Main ###

main()
