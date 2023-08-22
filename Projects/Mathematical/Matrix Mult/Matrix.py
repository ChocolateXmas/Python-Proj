##################################
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##
## Created by: Alex Beigel      ##
## Date: 20.05.23               ##
## Program: Matrix.py           ##
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##
##################################

# Will get a list of lists that represents a Matrix, and returns a Transposed Version of itself.
# The functions assumes that the matrix is legit & as a result can be transposed.
### - NOTE: Any exceptions will have to be caught - ###
def transpose_mat(mat):
    return [ [mat[row][col] for row in range(len(mat)) ] for col in range(len(mat[0])) ]
### END transpose_mat ###

# Returns a multiplication matrix of Matrix A * Matrix B.
# The functions assumes that both matrices legit & can be multiplicated by Matrices Math Mult Laws.
### - NOTE: Any exceptions will have to be caught - ###
def mult_matrix(A, B):
    return [ [ sum(A[row][row_b]*B[row_b][col] for row_b in range(len(B))) for col in range(len(B[0])) ] \
             for row in range(len(A)) ]
### END mult_matrix ###

# Returns the maximus number in a matrix
def max_value(Mat_A):
    return max( max(row) for row in Mat_A )
### END max_value ###

# This function returns True if the given matrix is legit by math laws, Else will return False
def is_matLegit(A):
    row_len = len(A[0])
    for row in A:
        if row_len != len(row):
            return False
    return True
### END is_matLegit ###

# Prints a matrix beautifully
def print_mat(mat):
    length = len(str(max_value(mat)))
    for row in range(len(mat)):
        for col in range(len(mat[row])):
            print(" "*( (length-len(str(mat[row][col])))//2 ) +
                  str(mat[row][col]) +
                  " "*( (length-len(str(mat[row][col])))//2 ), end=" ")
        print()
### END print_mat ###

def main():
    try:
        file = open("matrices.txt", "r")
        lines = file.readlines()
        file.close()
    except FileNotFoundError:
        print("> File does not exist !")

    if len(lines) == 0:
        print("> File is EMPTY !")
    else:
        print("> Values: ")
        print(*lines, sep="")
        print("\nAfter\n")
        mat_lst = [ [], [] ]  # A list with 2 cells, that every cell assembles a matrix
        mat_count = -1
        try:
            for i in range(len(lines)):
                # if lines[i][-2] != "=":
                if lines[i].find("=") == -1:
                    try:
                        mat_lst[mat_count].append(list(map(int, [*lines[i].split()])))
                    except ValueError as e:
                        print("~ Cant cast to int !")
                        print(e)
                else:
                    mat_count += 1
            A_flag, B_flag = is_matLegit(mat_lst[0]), is_matLegit(mat_lst[1])
            if A_flag and B_flag:
                print("> Matrix 'A':")
                print_mat(mat_lst[0])
                print("> Matrix 'B:")
                print_mat(mat_lst[1])
                print("> Multiplication A*B :")
                mult = mult_matrix(mat_lst[0], mat_lst[1])
                print_mat(mult)
                print("> Transposed (AB)ᵗ :")
                print_mat( transpose_mat(mult) )
            elif not A_flag:
                print("> Matrix 'A' is not legit by Math Laws !")
            elif not B_flag:
                print("> Matrix 'B' is not legit by Math Laws !")
        except Exception as e:
            print("> Text File is not written good")
            print(e)
### END main ###

main()