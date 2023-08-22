##################################
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##
## Created by: Alex Beigel      ##
## Date: 20.05.23               ##
## Program: Grades.py           ##
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##
##################################

# Gets a list of lines from students.txt file
# Returns a dictionary where key=ID, value=Full Name
def read_students(lst):
    return { lst[i].split()[0]:lst[i].split()[1] + " " + lst[i].split()[2] for i in range(len(lst)) }
### END read_students ###

# Get a list of lines from grades.txt
# Returns a dictionary where key=ID, value=Student's Grade
def read_grades(lst):
    return { lst[i].split()[0]:lst[i].split()[1] for i in range(len(lst)) }
### END read_grades ###

# Gets a ID:Grades dict
# Returns Average of all the grades of students
def average_grades(grades_dict):
    return sum( map(int, grades_dict.values()) ) / len(grades_dict)
### END average_grades ###

# Return a list of student's names that have the highest grade in Student's Dict
def find_max(s_dict, g_dict):
    verified_grades = verify_ids(s_dict, g_dict)
    max_lst = []
    max_g = max(verified_grades.values())
    for (key, value) in verified_grades.items():
        if value == max_g:
            max_lst.append(s_dict[key])
    return max_lst, max_g
### END find_max ###

# Gets both Students & Grades Dicts and removes the ID's from the grades that are not in Students
def verify_ids(s_dict, g_dict):
    new_g = dict(g_dict)
    for ID in g_dict:
        try:
            s_dict[ID]
        except:
            new_g.pop(ID)
            print(f"{ID} is not in Students! ")
    return new_g
### END verify_ids ###

def main():
    students_file = ""
    grades_file = ""
    ### Try open students.txt ###
    try:
        file = open("students.txt", "r")
        students_file = file.readlines()
        file.close()
    except FileNotFoundError as e:
        print("> Students file not found !")
    ### Try open grades.txt ###
    try:
        file = open("grades.txt", "r")
        grades_file = file.readlines()
        file.close()
    except FileNotFoundError as e:
        print("> Grades file not found !")
    student_dict = dict()
    grades_dict = dict()
    # will continue the program if both files aren't empty, else will quit
    if len(students_file) and len(grades_file) != 0:
        # print(*students., sep="")
        # print(students[0].split()[0])
        try:
            student_dict = read_students(students_file)
            grades_dict = read_grades(grades_file)
        except IndexError as e:
            # If the file isn't written good, checks if theres less info than needed
            print(e)
        avg = average_grades(grades_dict)
        print("> Average Grades:", avg)
        max_s, max_g = find_max(student_dict, grades_dict)
        print("Max Grade: " + "< " + str(max_g) + " >")
        # print("> ",*max_s, sep="\n")
        for s in max_s:
            print(">", s)
            # print("Verfied: ", verify_ids(student_dict, grades_dict, True))
### END main ###

main()