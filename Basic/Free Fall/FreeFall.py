##################################
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##
## Created by: Alex Beigel      ##
## Date: 14.03.23               ##
## Program: FreeFall.py         ##
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##
##################################

# FreeFall
# This Function gets a parameter of Height (h) that shows the height of a rock.
# It will calculate the time in seconds and the velocity of Meters per Seconds using a Physics Equation.
G = 9.8 # Gravity
def FreeFall(h):
    T = ( (2 * h) / G ) ** 0.5 # Time in second to fall
    V = G * T # Velocity
    print("> Time to fall: " + "%.2f" % T + " Seconds \n> Velocity: " + "%.2f" % V + " Meter/sec")

def main():
    # H = Height in meters, can be a int or a float, but we will cast it into float automatically as a float number
    # can also be int, for example: 9.0
    H = float(input("> Please enter the height of the rock in meters: "))
    FreeFall(H)

main()
