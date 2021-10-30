import math


def distance(x1, x2, y1, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)


R, X, Y = map(int, input().split())

d = distance(0, X, 0, Y)


if not R == d and d <= 2*R:
    print(2)
else:
    print(math.ceil(d/R))
