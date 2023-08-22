##################################
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##
## Created by: Alex Beigel      ##
## Date: 12.06.23               ##
## Program: MakeList.py         ##
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##
##################################

# Will accept only Integers for input
def custom_int_input():
    while n := input(">Number: _"):
        # print("D")
        try:
            if int(n) >= 1:
                break
            else:
                raise ValueError
        except ValueError as e:
            print("> Only Integers bigger than 1 (include) are allowed. . .")
    return int(n)
### END custom_int_input ###

def makelist(n):
    lst = []
    if n == 1:
        return [[n]]
    else:
        previous_list = makelist(n - 1)
        current_list = previous_list[-1] + [n]
        return previous_list + [current_list]
### END makelist ###

def main():
    num = custom_int_input(  )
    print(makelist(num))
## END main ###

if __name__ == "__main__":
    main()