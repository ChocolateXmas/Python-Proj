##################################
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##
## Created by: Alex Beigel      ##
## Date: 12.06.23               ##
## Program: minesweeper.py      ##
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##
##################################
import random

Game_Title = f" |_   \  /   _|(_)             .' ____ \ \n" + \
             f"   |   \/   |  __  _ .--. .---.| (___ \__   _   __ .---. .---. _ .--.  .---. _ .--.  \n" + \
             f"   | |\  /| | [  |[ `.-. / /__\\_.____`[ \ [ \ [  / /__\/ /__\[ '/'`\ / /__\[ `/'`\] \n" + \
             f"  _| |_\/_| |_ | | | | | | \__.| \____) \ \/\ \/ /| \__.| \__.,| \__/ | \__.,| |     \n" + \
             f" _____||_____[_______||______.'\______.'\__/\__/  '.__.''.__.'| ;.__/ '.__.[___]     \n" + \
             f" |_  _| |_  _|  /  |   .'    '.                               [__|                   \n" + \
             f"   \ \   / _____`| |  |  .--.  |                                                     \n" + \
             f"    \ \ / |______| |  | |    | |                                                     \n" + \
             f"     \ ' /      _| |_ |  `--'  |                                                     \n" + \
             f"      \_/      |_____(_'.____.'                                                      \n"


class MineSweeper:
    __Ms_main_menu = "\n\n~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~\n" + \
                     "~=- ~ = - > Mine - Sweeper V1.0 < - = ~ -=~\n" + \
                     ">>> Choose your option :\n" + \
                     "1. Start Game ! \n" + \
                     "2. ✮ ✮ ✮ ScoreBoard ✮ ✮ ✮ \n" + \
                     "99. Quit !"

    # - ATTRIBUTES - #
    # __mineBoard -> Holds the board with mines and numbers, but doesn't show them !
    # __gameBoard -> Holds the playable board, will show the chosen cells by user
    def __init__(self):
        self.__ActiveGame = False  # If user is playing will change to True
        self.__mineBoard = []  # Hidden - 2Dim List Includes all the numbers and mines
        self.__gameBoard = []  # Shown - Only the choice on Board of user's view
        self.__padBoard = []  # Hidden - Meant for calculations only!
        self.__size = None
        self.__MaxMines = None
        self.__level_count = None
        self.__game_level_title = "-> Level: " + str(self.__level_count) + "\n# Game Board: "
        self.__Title = " ___  ___ _               _____\n" + \
                       " |  \/  |(_)             /  ___|\n" + \
                       " | .  . | _  _ __    ___ \ `--. __      __  ___   ___  _ __   _ __\n" + \
                       " | |\/| || || '_ \  / _ \ `--. \\ \ /\ / / / _ \ / _ \| '_ \ | '__|\n" + \
                       " | |  | || || | | ||  __//\__/ / \ V  V / |  __/|  __/| |_) || |\n" + \
                       " \_|  |_/|_||_| |_| \___|\____/   \_/\_/   \___| \___|| .__/ |_|\n" + \
                       "                                                      | |\n" + \
                       "                                                      |_|\n"
    ### END __int__ ###

    # Run Game Loop #
    def Start(self):
        self.__set_setting()  # Boards Initialized !
        self.__level_count = 1
        print(self.__game_level_title)  # Show first EMPTY board
        print(self)  # < < -------------|
        # *NOTE: Next game boards prints will be handled by __makeMove() inner function
        # Input cell (row, col) for 1st time
        row = self.__custom_int_input("> Row: _", 1, len(self.__gameBoard))
        col = self.__custom_int_input("> Col: _", 1, len(self.__gameBoard))

        while self.__makeMove(row, col):
            row = self.__custom_int_input("> Row: _", 1, len(self.__gameBoard))
            col = self.__custom_int_input("> Col: _", 1, len(self.__gameBoard))
    ### END Start() ###

    # Gets a row & col indexes and checks the wanted cell
    def __makeMove(self, row, col): # Human Reading Format

        def nextMove(): # Responsible for level counting and board printing
            self.__print_inGameTitle() # Prints Game Level Title
            print(self) # Prints Game Board
        ### END nextMove() ###

        if self.__gameBoard[row - 1][col - 1] == " ":
            if self.__mineBoard[0][0] == " ":  # First time choosing a cell
                self.__set_randomMines(row, col, int( self.__MaxMines ))  # Will NOT Put a mine in the given cell
                self.__fillNumbers()  # Set board with values
                self.__showCell_Recursive(row-1, col-1) # Recursive # (row/col Numbers are in human reading mode)
                nextMove()
                return True  # Continue
            elif self.__mineBoard[row - 1][col - 1] == "X":  # > User chose Mine < #
                self.__showMines() # > User Has lost < #
                nextMove()
                print("\n\n#,~< -: GAME OVER :- >~,#\n\n")
                print(f">>> You Survived {self.__level_count} Rounds !")
                return False  # ,~< -: GAME OVER :- >~,#
            elif self.__mineBoard[row - 1][col - 1] != "X":  # User chose a Number
                # TODO: Make a Recursive function to show all the neighbor cell with numbers
                self.__showCell_Recursive(row-1, col-1) # Recursive # (row/col Numbers are in human reading mode)
                self.__level_count += 1
                if self.__CheckWin():  # WIN !
                    # print(self.__print_Board(self.__mineBoard))
                    print(self)
                    print(f">>> You WON! Only {self.__level_count} Rounds !")
                    return False  # Continue
                nextMove()
                return True  # continue
        else:
            print(f"> Cell ({row},{col}) is already chosen! Choose another . . ")
            return True # Continue to next iteration
    ### END __makeMove() ###

    # row/col are in human reading mode, it's fine for the __paddedBoard
    def __showCell_Recursive(self, row_index, col_index):
        # print("> Added to game board ")
        self.__gameBoard[row_index][col_index] = self.__mineBoard[row_index][col_index]  # Show the cell

        neighbors_pos = [ (row_index-1, col_index-1),  (row_index-1, col_index),  (row_index-1, col_index+1),
                          (row_index  , col_index-1),                             (row_index  , col_index+1),
                          (row_index+1, col_index  ),  (row_index+1, col_index),  (row_index+1, col_index+1) ]

        if self.__padBoard[row_index + 1][col_index + 1] == 0:
            # Check its neighbors
            for neighbor_pos in neighbors_pos:
                r_pos, c_pos = neighbor_pos
                if 0 <= r_pos < len(self.__padBoard) - 2 and 0 <= c_pos < len(self.__padBoard[0]) - 2:
                    if self.__gameBoard[r_pos][c_pos] != self.__mineBoard[r_pos][c_pos]:
                        self.__showCell_Recursive(r_pos, c_pos)
    ### END __showCell_Recursive() ###

    # > User Has lost < # hence -> will show all the mines on the game board
    def __showMines(self):
        for r_index in range(len(self.__gameBoard)):
            for c_index in range(len(self.__gameBoard[r_index])):
                if self.__mineBoard[r_index][c_index] == self.__gameBoard[r_index][c_index]:
                    continue
                else:  # Meaning cell -> " "
                    self.__gameBoard[r_index][c_index] = x \
                        if (x := self.__mineBoard[r_index][c_index]) == "X" \
                        else " "
                # elif self.__gameBoard[r_index][c_index]

    def __CheckWin(self):
        for r_values in self.__gameBoard:
            super_row_index = self.__gameBoard.index(r_values)
            counter = r_values.count(" ")
            if counter == 0:
                continue
            elif counter == 1:
                if self.__mineBoard[super_row_index] \
                        [self.__gameBoard[super_row_index].index(" ")] == "X":
                    continue
                else:
                    return False
            else:
                return False
        return True
    ### END __CheckWin() ###

    # Meant to fill numbers of neighbors for first time
    def __fillNumbers(self):
        for r in range(len(self.__mineBoard)):
            for c in range(len(self.__mineBoard[r])):
                if self.__mineBoard[r][c] != "X":
                    m_count = self.__count_mines(r, c)  # Mines_Count
                    self.__mineBoard[r][c] = m_count
                    self.__padBoard[r + 1][c + 1] = m_count
    ### END __fillNumbers() ###

    def __get_maxMines(self):
        return int(self.__MaxMines)

    def __set_randomMines(self, row, col, max_mines):
        if max_mines == 0:
            return
        else:
            r, c = random.randint(0, len(self.__mineBoard) - 1), random.randint(0, len(self.__mineBoard) - 1)
            # print("r,c: ", r,c)
            if (r + 1 == row and c + 1 == col) or self.__mineBoard[r][c] == "X":
                # Recursive action to check other cell that if the chosen cell is a Mine
                self.__set_randomMines(row, col, max_mines)
            else:
                self.__mineBoard[r][c] = "X"
                self.__padBoard[r + 1][c + 1] = "X"
                # Recursive action to fill next mines
                self.__set_randomMines(row, col, max_mines - 1)
    ### END __set_randomMines() ###

    #  - Initialization -  #
    def __set_setting(self):
        # Board Size Value #
        self.__size = self.__custom_int_input("> Board size: _", 3, 9)
        self.__MaxMines = self.__custom_int_input("> Mines Amount: _", 2, 2 * self.__size - 1)
        self.__level_count = 1
        # Initialize: Game&Calculation boards #
        self.__mineBoard = [[" " for i in range(int(self.__size))] for j in range(int(self.__size))]
        self.__padBoard = self.__padded_board(self.__mineBoard)  # Creates a padded board to avoid Index Errors
        self.__gameBoard = [[" " for i in range(int(self.__size))] for j in range(int(self.__size))]
        # self.__MaxMines = random.randint(2*self.__size - 3, 2*self.__size - 1)
    ### END __set_setting() ###

    # Gets -> the original current generation list
    # Return -> Padded list to avoid IndexError out of boundaries
    def __padded_board(self, lst):
        padded_lst = [[" " for i in range(0, len(lst[0]) + 2)]]
        for r_index in lst:
            padded_lst.append([" ", *r_index, " "])
        padded_lst.append(padded_lst[0])  # Line of Zero's
        return padded_lst

    ### END padded_board ###

    # Gets -> Row and Col indexes of the original current board
    # Return - > how many "live" neighbor cells are there in the 8 cells around it
    def __count_mines(self, row_index, col_index):
        # Incrementing the indexes because we added more lines and cols in the pad_lst
        row_index += 1
        col_index += 1
        neighbor_count = 0
        # r1 & c1 are calculation index for checking neighbors
        r1 = -1
        c1 = -1
        for i in range(3):  # checks 3 rows
            for j in range(3):  # Checks 3 cols
                # We don't want to check the given cell @ (0, 0) ;)
                # But will check if it's alive, meaning equals "1"
                if (r1, c1) != (0, 0):
                    if self.__padBoard[row_index + r1][col_index + c1] == "X":
                        neighbor_count += 1
                c1 += 1
            r1 += 1  # Next row increment
            c1 = -1  # Returning to default col index calculation (Checks from Left to Right)
        return neighbor_count

    ### END __count_mines() ###

    def __custom_int_input(self, s2input, min_value, max_value):
        while type(n := input(s2input)) is str:
            try:
                if n.isdigit() and min_value <= int(n) <= max_value:
                    # if min_value <= int(n) <= max_value:
                    break
                else:
                    raise ValueError
            except ValueError:
                print(f"> Only Integers between <{min_value}> & <{max_value}> (include) are allowed. . .")
        return int(n)

    ### END custom_int_input ###

    # Prints any chosen board, Private use only #
    def __print_Board(self, board):
        if board is None:
            return "> Game board is not initialized !"
        else:
            s2p = ""
            table_str = " " + "+---" * len(board) + "+"
            s2p += table_str + "\n"
            for row in range(len(board)):
                s2p += f"{row + 1}|"
                for col in range(len(board[row])):
                    s2p += f' {board[row][col]} |'
                s2p += "\n" + table_str + "\n"
            # To show col indexes beneath the game board
            for i in range(len(board)):
                s2p += "   " + str(i + 1)
            return s2p

    ### END print_mines ###

    # Return -> Title String
    def get_Title(self):
        return self.__Title
    ### END get_Title() ###

    def __print_inGameTitle(self):
        print(f"-> Level: " + str(self.__level_count) + "\n# Game Board: ")
    ### END __print_inGameTitle() ###

    # Only prints the board with user's choices
    def __str__(self):
        if self.__mineBoard is None:
            return "> Game board is not initialized !"
        else:
            s2p = ""
            table_str = " " + "+---" * len(self.__gameBoard) + "+"
            s2p += table_str + "\n"
            for row in range(len(self.__gameBoard)):
                s2p += f"{row + 1}|"
                for col in range(len(self.__gameBoard[row])):
                    s2p += f' {self.__gameBoard[row][col]} |'
                s2p += "\n" + table_str + "\n"
            # To show col indexes beneath the game board
            for i in range(len(self.__gameBoard)):
                s2p += "   " + str(i + 1)
            return s2p
    ### END __str__ ###


### END MineSweeper Class ###


class Game:
    __Game_main_menu = "\n\n~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~\n" + \
                       "~=- ~ = - > ! R3tro Game$ ! < - = ~ -=~\n" + \
                       ">>> Choose your option :\n" + \
                       "1. Start Game ! \n" + \
                       "2. ✮ ✮ ✮ ScoreBoard ✮ ✮ ✮ \n" + \
                       "99. Quit !"

    def __init__(self):
        print(Game_Title)
        self.__MnSpr = MineSweeper()
        self.__score_board = None
        self.__Menu = (1, 2, 99)
    ### END __init__ ###

    ##################################
    ## "r" - Read - Default value. Opens a file for reading, error if the file does not exist
    ## "a" - Append - Opens a file for appending, creates the file if it does not exist
    ## "w" - Write - Opens a file for writing, creates the file if it does not exist
    ## "x" - Create - Creates the specified file, returns an error if the file exists
    ##################################
    def Start(self):
        # to load up scoreboard at
        try:
            file = open("srbd.txt", "r")
            score_lines = file.readlines()
            file.close()
        except FileNotFoundError:
            file = open("srbd.txt", "a")
            score_lines = file.readlines()
            file.close()

        print(self.__Game_main_menu)
        option = str(input("$ Enter your choice: \n"))
        while option != "99":
            # print("Does it exist ? :", self.__check_option(option))
            # print(option)
            if option == "1":
                print("Option:", option)
                print(self.__MnSpr.get_Title())
                self.__MnSpr.Start()
            elif option == "2":  # Show Score Board
                print("Option:", option)
                print(" < < < Coming Soon ! . . . > > >")
                # print(self.__check_srbd(score_lines))
            else:
                print("> Didn't quite get your choice... TRY AGAIN ;-) ")
                option = str(input("$ Enter your choice: \n"))
                continue
            print(self.__Game_main_menu)
            option = str(input("$ Enter your choice: \n"))
        # while option
        quit()

    ### END Start() ###

    # Check for scoreboard file and scan if if it has some data
    # Input  -> text
    # Return -> score board Text
    # TODO: Make a scoreboard check
    def __check_srbd(self, text):
        __limits = ("{", "}", "[", "]")
        __scores = []
        if all(x in text for x in __limits):
            # if the text has all the characters of limits in it, so we can build a score board
            # return " >>> Filled with DATA"
            # TODO: Start checking scores, build a list of scores with all data if everything's in the right order
            pass
        else:
            # otherwise, make a new empty scoreboard with default highscores
            # {NAME}[Time](Size)
            # NAME : User's nickname, max 8 chars !
            # Time : How long the game took
            # Size : WIll be shown & ordered by boards size
            # DEFAULT: {KingAce}[200](5)
            # TODO: Make a new Scoreboard with default highscores to beat ;)
            pass

    ### END __check_srbd() ###

    def __read_scores(self):
        pass
    ### END read_scores() ###

    def __insert_score(self, nickname, time, size):
        pass
    ### END insert_score() ###

    def __str__(self):
        return self.__MnSpr.get_Title()
    #     return self.__str__()
### END Game Class ###

def main():
    newGame = Game()
    newGame.Start()
### END main() ###

if __name__ == "__main__":
    main()
