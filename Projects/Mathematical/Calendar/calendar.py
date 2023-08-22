##################################
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##
## Created by: Alex Beigel      ##
## Date: 22.04.23               ##
## Program: Calendar.py         ##
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##
##################################

import random as rnd

### SOME FACTS . . . ###
### Special Dates - These dates are sharing the SAME DAY of the week, Every year any time ! ###
# 4 / 4
# 6 / 6
# 8 / 8
# 10 / 10
# 12 / 12
# Doomsdays:
# 5 / 9
# 9 / 5
# 7 / 11
# 11 / 7
# -> PI DAY ! : 14 / 3 Also Shares the same day as all the other special dates !
# As for the January and February months:
#        Regular Year : Leap Year
# January  - (3 / 1)  : (4 /1)
# February - (28 / 2) : (29 / 2)
#################################
# Where it all started... In this year we have really started counting, because of the 11 days lag we can't be sure
# What was the day in the week before that year.
# Started = 1753

# A Final List of Months Names
# Months[*][2] - Means every 3rd member of the month's row assembles a code, it's necessary for further calculations.
# REMEMBER ! In a leap year the code for January is (5) and for February is (1)
Months = [ ["January", 31, 0],
           ["February", 28, 3],
           ["March", 31, 3],
           ["April", 30, 6],
           ["May", 31, 1],
           ["June", 30, 4],
           ["July", 31, 6],
           ["August", 31, 2],
           ["September", 30, 5],
           ["October", 31, 0],
           ["November", 30, 3],
           ["December", 31, 5] ]

# A Final list of Weed Days shortened names
# An index of this list will present the day of the week
# I.E : index=0 : Sunday, index=5 : Friday etc...
WeekDays = ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"]
wd = "  ".join(WeekDays)

# "BONUS" OBJECT - If the user inputs wrong date format 3 times, then will be printed a helper format to show how it is
# supposed to look like.
num_of_try: int = 0
# This function gets a string and checks whether it includes a Month name & Year in it.
# Spaces and Apostrophes are not taken in account.
def checkDate(string):
    def findMonth(str2check):
        for mnt in Months:
            if str2check.upper() == mnt[0][0:len(str2check)].upper():
                # Exist !
                return True, Months.index(mnt)
        return False, None
    global num_of_try
    def resetTry():
        global num_of_try
        num_of_try = 0
    # End resetTry() #
    def showExample():
        global num_of_try
        print("> Ayo, u need to type a right date format ! ")
        if num_of_try < 3:
            num_of_try += 1
        else:
            m = Months.index( rnd.choice(Months) )
            y = rnd.randint(1900, 2026)
            print("> If you're not getting along, here's an example for how it should look like: \n",
                  "('", Months[m][0], y, "') ", "OR", "('", Months[m][0][0:3], y, "') ")
    # End showExample() #
    m_flag, m_index = False, int() # Temporary objects that will contain data
    st = str(string)
    st = st.upper().strip().split()
    # Needs to be only -Month name-, -Year- (IN THAT ORDER) to show the calendar.
    if len(st) == 2:
        # If the Month length is more than 3.
        # I.E. "October"
        if len(st[0]) < 3:
            # No Match for months, because there's no such month with less than 3 letters
            showExample()
        elif len(st[0]) >= 3:
            m_flag, m_index = findMonth(st[0]) # Need to check if we found a legit month name
            if m_flag and st[1].isdigit():
                resetTry()
                cal(m_index, st[1])
            else:
                # If no Month name found or/and isnt a year than show example
                showExample()
    else:
        showExample()
### END checkDate ###

# This Function gets a Year value of int() and calculates whether it is a leap year or nah
def checkLeapYear(year):
    # If divided by 400 => Leap Year
    if int(year) % 400 == 0:
        return True
    # If divided by 100 => NOT A Leap Year
    elif int(year) % 100 == 0:
        return False
    # If divided by 4 and not by 100 and 400  => Leap Year
    elif int(year) % 4 == 0:
        return True
    # If nothing from above, then it isn't a leap year
    else:
        return False
### END checkLeapYear ###

# For calculations, this function will simply return the code of the given month index from Months list.
def checkMonthCode(month_index):
    return Months[month_index][2]
### END checkMonthCode ###

# Return the Year code, Formula: <<< (YY + (YY div 4)) mod 7 >>>
def checkYearCode(year):
    return ( int(str(year)[-2]+str(year)[-1]) + ((int( str(year)[-2]+str(year)[-1] ))//4) ) % 7
### END checkYearCode ###

# Every century has a code, the code is repetitive every 400 years in the Gregorian Calendar
# 1700s = 4
# 1800s = 2
# 1900s = 0
# 2000s = 6
# 2100s = 4
# 2200s = 2
# 2300s = 0, and so on...
# These codes are important for later calculations.
def checkCenturyCode(year):
    try:
        if 1700 <= int(year) <= 1799:
            return 4
        elif 1800 <= int(year) <= 1899:
            return 2
        elif 1900 <= int(year) <= 1999:
            return 0
        elif 2000 <= int(year) <= 2099:
            return 6
        else:
            return checkCenturyCode(year - 400) if year > 1699 else checkCenturyCode(year + 400)
    except:
        print("> Wrong type man")
### END checkCenturyCode ###

# With a given month and year, this function will return an index of the 1 Day of that month in the week.
# As well this function will calculate & check for month,year and leap year codes for result.
# Formula: <<< (Year Code + Month Code + Century Code + Date Number - Leap Year Code) mod 7 >>>
def checkDayOfWeek(day, month, year):
    return ( checkYearCode(int(year)) + checkMonthCode(month) + checkCenturyCode(year) + int(day) - int(checkLeapYear(int(year))) ) % 7
### END checkDayOfWeek ###

# This function gets a month and a year and shows the calendar for that specific date.
# IF the user also inputs a month day(i.e. 20 of july 1998),
# THEN the function will print the Day Of The Week of that given DATE.
# Formula: <<< (Year Code + Month Code + Century Code + Date Number - Leap Year Code) mod 7 >>>
def cal(month_num, year):
    print(Months[month_num][0], year)
    print(wd) # wd is the object referenced to a concatenated string of shorted week days.
    leap_flag = checkLeapYear(int(year))
    calendar_string = "" # The calendar matrix string to print
    where2start = checkDayOfWeek(1, month_num, int(year)) # Will represent from which day in week to start from
    calendar_string += "    " * where2start
    day_amount = Months[month_num][1]
    # If its a leap year and wanted
    if leap_flag and month_num == 1:
        day_amount += 1
    for day in range(1, (day_amount+1)):
        # if where2start % 6 == 0:
        #     calendar_string += "\n"
        if day >= 10:
            calendar_string += str(day)
        else:
            calendar_string += str(day) + " "
        # print("len cal st: ", len(calendar_string))
        if where2start % 6 == 0 and where2start != 0:
            calendar_string += "\n"
            where2start = 0
            continue
        else:
            calendar_string += " "*2
        where2start += 1
    print(calendar_string)
### END cal ###

def main():
    st = ""
    while st != "stop":
        st = str(input("> Plz Enter a Date ('stop' to END) : {_ "))
        checkDate(st)
### END Main ###

main()