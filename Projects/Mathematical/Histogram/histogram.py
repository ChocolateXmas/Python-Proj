##################################
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##
## Created by: Alex Beigel      ##
## Date: 22.04.23               ##
## Program: Histogram.py        ##
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##
##################################

# A list that will create 26 elements that each will represent the Lower English ABC AlphaBet
# the chars will be created through ascii codes
alphaBet = [chr(i + 97) for i in range(26)]

# ASCII
# "a" -> 97 :: "z" --> 122
# ord("a")-97 == 0
# ord("z")-97 == 25
def count_letters(s):
    # List of counters for every char in the English Alfabet - Ordered
    histoList = [0 for i in range(26)]
    new_s = str(s).lower().split()
    for c in range(0, len(new_s)):
        for i in range(0, len(new_s[c])):
            if 97 <= ord(new_s[c][i]) <= 122 and new_s[c].find((new_s[c][i]), 0, i) == -1:
                histoList[ord(new_s[c][i].lower()) - 97] += 1
        # string.find((new_s[c]), 0, i)
        # if 97 <= ord(new_s[c]) <= 122:
        #     histoList[ord(new_s[c].lower())-97] += 1
    return histoList
### END count_letters ###

def draw_histogram(count_list):
    graph = ' '.join(char for char in alphaBet)
    line = ""
    for i in range(0, max(count_list)):
        for c in range(0, len(count_list)):
            if count_list[c] != 0:
                line += "^ "
                count_list[c] -= 1
            else:
                line += "  "
        graph = line + "\n" + graph
        line = ""
    return graph
### END draw_histogram ###

def main():
    # print(count_letters("this is a test for counting letters in words and drawing a histogram"))
    # print(draw_histogram(count_letters("this is a test for counting letters in words and drawing a histogram")))
    print("> Hello, and welcome to <:Histogram:>")
    option = ""
    while option != "exit!":
        print("> (DEFAULT: *.txt)\n> Please Enter a file name for action ('exit!' to finish)")
        option = input("> File Name: ")
        if option == "exit!":
            break
        try:
            file = open(str(option) + ".txt", "r")
            lines = file.read()
            file.close()
            print(">>> Histogram of " + str(option) + ".txt :\n")
            print(draw_histogram(
                count_letters(lines)
            ))
        except FileNotFoundError:
            print("> File does not exist! ")
            option = input("> Would you like to continue searching? Y / N _")
            if option.lower() == "n":
                break
            elif option.lower() == "y":
                continue
            else:
                print("Hmmm.....")
            # continue if option.lower() == "y" else break
### END main ###

main()
