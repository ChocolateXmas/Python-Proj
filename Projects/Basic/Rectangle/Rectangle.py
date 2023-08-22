##################################
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##
## Created by: Alex Beigel      ##
## Date: 14.03.23               ##
## Program: Rectangle.py        ##
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##
##################################

# Rectangle.py
# This Function gets a character and a number that the user decides, and print a 4-row rectangle that's
# made of the given character.
def Rectangle(char, num):
    print(char*num)
    print(char + " " * (num - 2) + char)
    print(char + " " * (num - 2) + char)
    print(char * num)

def main():
    Rect_Char = str(input("-> Enter a wanted character: "))
    Rect_Num = int(input("-> Enter a wanted lenth: "))
    Rectangle(Rect_Char, Rect_Num)

main()