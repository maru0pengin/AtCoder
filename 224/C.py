import itertools


def men(a, b, c):
    # (x1-x3)*(y2-y3)-(x2-x3)*(y1-y3)
    return abs((a[0]-c[0])*(b[1]-c[1])-(b[0]-c[0])*(a[1]-c[1]))/2


N = int(input())
XY = []
for _ in range(N):
    x, y = map(int, input().split())
    XY.append([x, y])


l = ['a', 'b', 'c', 'd']

com = list(itertools.combinations(XY, 3))

result = 0
for i in range(len(com)):
    a = com[i][0]
    b = com[i][1]
    c = com[i][2]

    if men(a, b, c) > 0:
        result += 1


print(result)
