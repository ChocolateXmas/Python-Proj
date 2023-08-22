##################################
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##
## Created by: Alex Beigel      ##
## Date: 20.05.23               ##
## Program: lifeGame.py         ##
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##
##################################

#### RULES ####
# At each step in time, the following transitions occur:
#   1.) Any live cell with fewer than two live neighbours dies, as if by underpopulation.
#   2.) Any live cell with two or three live neighbours lives on to the next generation.
#   3.) Any live cell with more than three live neighbours dies, as if by overpopulation.
#   4.) Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
#
# These rules, which compare the behaviour of the automaton to real life, can be condensed into the following:
#   1.) Any live cell with two or three live neighbours survives.
#   2.) Any dead cell with three live neighbours becomes a live cell.
#   3.) All other live cells die in the next generation. Similarly, all other dead cells stay dead.
import random

def createFileContent():
    text = ""
    txt_input = None
    while txt_input != "":
        txt_input = input()
        if txt_input != "":
            text += txt_input + "\n"
        else:
            # Removing any new lines ("\n") at the end of the string
            text = text[:-1]
    return text
### END createFile ###

# Checks if the generation is a 'Y' rows on 'Y' cols board
def validate_genSize(lst):
    col_len = len(lst[0])
    for row in range(1, len(lst)):
        if len(lst[row]) == col_len:
            continue
        else:
            return False
    return True
### END validate_gen ###

# Checks if the board is only made from one's and zero's
def validate_genValues(lst):
    for row in range(0, len(lst)):
        for col in range(0, len(lst[row])):
            if lst[row][col] == "1" or lst[row][col] == "0":
                continue
            else:
                return False
    return True
### END validate_genValues ###

# Creates a random generation -> Type:(List)
def createRandom(rows, cols):
    return [ [str(random.randint(0, 1)) for col in range(cols)] for row in range(rows) ]
    # return [ [random.choice(arr) for col in range(x)] for row in range(x) ]
### END createRandom ###

# Prints the given Generation beautifully
live_cell:str = "|"
dead_cell:str = "o"
def print_gen(lst):
    for row in range(len(lst)):
        for col in range(len(lst[row])):
            if lst[row][col] == "1":
                # print(f'|{lst[row][col]}|', end="")
                print(f'({live_cell})', end="")
            else:
                # print(f' {lst[row][col]} ', end="")
                print(f' {dead_cell} ', end="")
        print()
    print()
### END print_gen ###

# Gets a list of the current generation and updates it to the next gen
def next_gen(lst):
    # Gets -> the original current generation list
    # Return -> Padded list to avoid IndexError out of boundaries
    def padded_board(lst):
        padded_lst = [ ["0" for i in range(0, len(lst[0])+2)] ]
        for r_index in lst:
            padded_lst.append(["0", *r_index, "0"])
        padded_lst.append( padded_lst[0] ) # Line of Zero's
        return padded_lst
    ### END padded_board ###

    pad_lst = padded_board(lst) # For calculations, a padded board

    # Gets -> Row and Col indexes of the original current board
    # Return - > how many "live" neighbor cells are there in the 8 cells around it
    def count_neighbours(row_index, col_index):
        # Incrementing the indexes because we added more lines and cols in the pad_lst
        row_index += 1
        col_index += 1
        neighbor_count = 0
        # r1 & c1 are calculation index for checking neighbors
        r1 = -1
        c1 = -1
        for i in range(3): # checks 3 rows
            for j in range(3): # Checks 3 cols
                # We don't want to check the given cell @ (0, 0) ;)
                # But will check if it's alive, meaning equals "1"
                if (r1,c1) != (0,0):
                    if pad_lst[row_index+r1][col_index+c1] == "1":
                        neighbor_count += 1
                c1 += 1
            r1 += 1 # Next row increment
            c1 = -1 # Returning to default col index calculation (Checks from Left to Right)
        return neighbor_count
    ### END count_neighbours ###

    new_lst = lst[:] # The next generation list
    #   1.) Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    #   2.) Any live cell with two or three live neighbours lives on to the next generation.
    #   3.) Any live cell with more than three live neighbours dies, as if by overpopulation.
    #   4.) Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    for r in range(len(lst)):
        for c in range(len(lst[r])):
            n_c = count_neighbours(r, c) # N_C -> Neighbour_Count
            if lst[r][c] == "0": # Current DEAD cell
                # 4.) Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
                if n_c == 3: # Reproduction
                    new_lst[r][c] = "1"
                # (***) Any other cell will continue to be dead on the next generation
                else:
                    new_lst[r][c] = "0"
            elif lst[r][c] == "1": # Current LIVE cell
                # 2.) Any LIVE cell with two or three live neighbours lives on to the next generation.
                if 2 <= n_c <= 3:
                    new_lst[r][c] = "1"
                # 1.) Any live cell with fewer than two live neighbours dies, as if by underpopulation.
                # 3.) Any live cell with more than three live neighbours dies, as if by overpopulation.
                else:
                    new_lst[r][c] = "0"
    lst = new_lst[:]
### END next_gen ###

# Reads a generation FROM a file
def create_genFromFile(file):
    txt = []
    for row in file.readlines():
        txt.append(list(map(str, row.split())))
    return txt
### END create_genFromFile ###

# Write a generation TO a file
def create_fileFromGen(file_name, gen_lst):
    try:
        txt = ""
        for row in range(len(gen_lst)):
            for col in range(len(gen_lst[row])):
                txt += str(gen_lst[row][col]) + " " if col != len(gen_lst[row])-1 else str(gen_lst[row][col]) + "\n"
        file = open(str(file_name), "w")
        file.writelines(txt)
        file.close()
    except Exception as e:
        print(e)
### END create_fileFromGen ###

# Gets -> current generation and
# Returns -> True if all the cells are dead, False if not
def is_dead(gen_lst):
    for row in range(len(gen_lst)):
        for col in range(len(gen_lst[row])):
            if gen_lst[row][col] == "1":
                return False
    return True # All cells are
### END is_dead ###

# This function STARTS the game & does all the needed function for calculations.
# Game ENDS when the generation is dead... :(
current_gen_str: str = "\n-------- Current Generation --------"
end_gen_str: str = "--------   End Generation   --------"
def Start_Game(gen_lst, gen_count=1):
    # gen_lst -> list() : Current generation of "Game Of Life"
    # gen_count -> int() : Starting value = 1, shows how many generations the game passed
    print(current_gen_str) # Title String
    print((" "+str(gen_count)+" ").center(len(current_gen_str), "~"), "\n") # Gen Counter
    print_gen(gen_lst) # Beautiful print of the current generation
    print(end_gen_str) # End Title String
    if not is_dead(gen_lst):
        c = str( input("> Continue? (Y/N)_ ") )
        next_gen(gen_lst)
        if c.upper() == "Y":
            return Start_Game(gen_lst, gen_count + 1)
    else:
        print("GAME OVER ! :P \n" 
              f'> Died after: ~ {gen_count} ~ Generations.')
        return None
    # print()
### END Start_Game ###

# BONUS #
# Changes the values of live & dead cells
def custom_values():
    global live_cell, dead_cell
    l_cell, d_cell = "", ""
    count_try = 0
    max_try = random.randint(1,4)
    while len(l_cell) != 1:
        try:
            if count_try < max_try:
                l_cell = str( input("> Live cell value: _") )
                if len(l_cell) != 1:
                    count_try += 1
                    raise Exception
            else:
                c = str( input("> Seems like you're troubled... Abort ? (Y/N) _") )
                if c.upper() == "Y":
                    print("> No values have changed ! ")
                    return None
                else:
                    count_try = 0
        except Exception as e:
            print("> Only characters with length of 1 are allowed !")
    # END l_cell While #
    count_try = 0
    while len(d_cell) != 1:
        try:
            if count_try < max_try:
                d_cell = str(input("> Dead cell value: _"))
                if len(d_cell) != 1:
                    count_try += 1
                    raise Exception
            else:
                c = str(input("> Seems like you're troubled... Abort ? (Y/N) _"))
                if c.upper() == "Y":
                    print("> No values have changed ! ")
                    return None
                else:
                    count_try = 0
        except Exception as e:
            print("> Only characters with length of 1 are allowed !")
    # END d_cell While #
    print(f'$ New values:\n> Live cell: {l_cell}\n> Dead cell: {d_cell}\n> Changes saved ! :D')
    live_cell, dead_cell = l_cell, d_cell
### END custom_values ###

# BONUS #
# Restores the live & dead cell values back to default -> ( live: o , dead: | )
def restore_values():
    global live_cell, dead_cell
    live_cell, dead_cell = "|", "o"
### END restore_values ###

def main():
    ### Variables: ###
    current_gen = None # Will always hold the current generation board
    ### END Variables ###

    def print_menu():
        print("\n> Welcome to Game Of Life !")
        print(">>> Choose your option :")
        print("1. Use an existing filename that u wrote \n"
              "2. Create a random generation \n"
              "3. Create a File that holds a new generation \n"
              "4. (~-~BONUS~-~) Customize LIVE & DEAD Cells !  \n"
              "5. (~-~BONUS~-~) Restore default values (live=o, dead=|||) !  \n"
              "99. Quit !")

    option = ""
    print_menu() # First time
    option = str( input("$ Enter your choice: \n") )
    while True:
        # Existing FileName
        if option == "1":
            try:
                file_name = str( input("> Enter File Name: \n") )
                file = open(file_name, "r")
                current_gen = create_genFromFile(file)
                file.close()
                # Size is not good
                if not validate_genSize(current_gen):
                    print("> Your board size is exceeding over it's limits, "
                          "make sure all rows and columns are well written ! ")
                    raise Exception
                # Values is not good
                elif not validate_genValues(current_gen):
                    print("> ONLY 1's and 0's are allowed in the board!")
                    raise Exception
                # Size & Values are fine, keep playing...
                else:
                    if len(current_gen) != 0:
                        Start_Game(current_gen)
                    else:
                        print("File is EMPTY !")
                        raise Exception
            except Exception as e:
                print(e)
                # print(f'>> Option 1 ERROR: \n-> {e} \n') ### DEBUG ###
                c = str( input("> Do u want to try another file?... (Y/N)_ ") )
                if c.upper() == "Y":
                    option = "1"
                    continue
        # Random Generated
        elif option == "2":
            print("Choice: ", option)
            try:
                rows = int( input("> Rows amount: _ ") )
                cols = int( input("> Cols amount: _ ") )
                if (rows or cols) <= 0:
                    raise ValueError
                current_gen = createRandom(rows, cols) # List of list for the random generation dawg
                create_fileFromGen("Game_Gen.txt", current_gen)
                Start_Game(current_gen)
            except ValueError as v:
                print("> Pretty awkward... :P \n> U need to enter only POSITIVE INTEGERS!")
                c = str(input("> Try Again ?... (Y/N)_ "))
                if c.upper() == "Y":
                    option = "2"
                    continue
        # Write a generation and automatically creates a file with it inside the console
        elif option == "3":
            # print("Choice: ", option)
            try:
                file_name = str(input("> Enter File Name: \n"))
                print("> * NOTE: if file exists, all the data wil be OVER-WRITTEN!\n"
                      "Please start writing your game board:")
                current_gen = createFileContent() # Plain Text !
                print(current_gen)
                # current_gen = create_genList(current_gen) # Cast to LIST
                # create_fileFromGen(file_name, current_gen)
                file = open(file_name, "w")
                file.write(current_gen)
                file.close()
            except Exception as e:
                print(e)
        elif option == "4":
            print("> Current values: \n"
                  f'> Live Cell: {live_cell}\n> Dead Cell: {dead_cell}')
            c = str( input("> Care to change ?... (Y/N)_ ") )
            if c.upper() == "Y":
                custom_values()
            # else:
            #     continue
        elif option == "5":
            restore_values()
            print("> Values have been restored !")
        elif option == "99":
            print("GG Well Played ;) ...")
            quit()
        else:
            print("> Didn't quite get your choice... TRY AGAIN ;-) ")
            option = str( input("$ Enter your choice: \n") )
            continue
        print_menu()
        option = str(input("$ Enter your choice: \n"))
    ### END while option ###
### END main ###

main()