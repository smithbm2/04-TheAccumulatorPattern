"""
This module lets you practice the ACCUMULATOR pattern in classic forms:
   SUMMING:    total = total + number
   COUNTING:   count = count + 1

A subsequent module lets you practice the ACCUMULATOR pattern
in another classic form:
   IN GRAPHICS:   x = x + pixels

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher, Mark Hays,
         Aaron Wilkin, their colleagues, and Braden Smith.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    x = 1
    y = 1
    if x == y:
        answer = True
    else:
        answer = False
    print(answer)
    print(type(answer))


main()

import rosegraphics as rg
r = 66
r2 = r
center = rg.Point(90, 40)
circle = rg.Circle(center, r)
r = 35
center.x = 200

print(r)
print(r2)
print(center)
print(circle)