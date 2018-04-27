import random as random


def newpoint():
    return random(-180, 180), random (-90, 90)

points = (newpoint() for x in range(500))
for point in points:
    print (point)