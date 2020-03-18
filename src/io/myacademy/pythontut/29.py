#Please write a function that calculates liquid volume in a sphere using the following formula.
# The radius r  is always 10, so consider making it a default parameter.
#vol = (4*pi*r^3/3) - (pi*h^2*(3r-h))/3
#set r = 10 and h = 2

import math

def calculateVolume(h, r=10):
    vol = (4 * math.pi * pow(r, 3) / 3) - (math.pi * pow(h, 2) * (3 * r - h) / 3)
    return vol

print(calculateVolume(2))