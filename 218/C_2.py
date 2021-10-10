N = int(input())
S = []
for i in range(N):
    s = list(input())
    S.append(s)

T = []
for i in range(N):
    t = list(input())
    T.append(t)


# ここまでで回転、ここから削る


def deleteY(directions, list):
    for _ in range(len(list)):
        for j in range(len(list[0])):
            if directions == "top":
                if list[0][j] == '#':
                    return
            if directions == "bottom":
                if list[-1][j] == '#':
                    return
        if directions == "top":
            list.pop(0)
        if directions == "bottom":
            list.pop(-1)


def deleteX(directions, list):
    for _ in range(len(list[0])):
        for j in range(len(list)):
            if directions == "left":
                if list[j][0] == '#':
                    return
            if directions == "right":
                if list[j][-1] == '#':
                    return

        if directions == "left":
            for i in range(len(list)):
                list[i].pop(0)
        if directions == "right":
            for i in range(len(list)):
                list[i].pop(-1)


# print(S)

directionYList = ['top', 'bottom']

directionXList = ['left', 'right']

for direction in directionYList:
    deleteY(direction, T)
    deleteY(direction, S)

for direction in directionXList:
    deleteX(direction, T)
    deleteX(direction, S)

n = len(S)
n2 = len(S[0])

S2 = [[] for _ in range(n2)]
S3 = [[] for _ in range(n)]
S4 = [[] for _ in range(n2)]

for i in range(n2):
    for j in range(n):
        S2[i].append(S[j][n2-i-1])

for i in range(n):
    s = list(reversed(S[n-i-1]))
    S3[i] = s

for i in range(n2):
    s = list(reversed(S2[n2-i-1]))
    S4[i] = s

# print(S)

if S == T or S2 == T or S3 == T or S4 == T:
    print("Yes")
else:
    print("No")
