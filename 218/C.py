N = int(input())
S = []
for i in range(N):
    s = list(input())
    S.append(s)

T = []
for i in range(N):
    t = list(input())
    T.append(t)


S2 = [[] for i in range(N)]
S3 = [[] for i in range(N)]
S4 = [[] for i in range(N)]

for i in range(N):
    for j in range(N):
        S2[i].append(S[j][N-i-1])

for i in range(N):
    s = list(reversed(S[N-i-1]))
    S3[i] = s

for i in range(N):
    s = list(reversed(S2[N-i-1]))
    S4[i] = s

# ここまでで回転、ここから削る

# T
Tflag = True
Sflag = True
S2flag = True
S3flag = True
S4flag = True


for _ in range(N):
    for j in range(N):
        if Tflag:
            if T[0][j] == '#':
                Tflag = False
        if Sflag:
            if S[0][j] == '#':
                Sflag = False
        if S2flag:
            if S2[0][j] == '#':
                S2flag = False
        if S3flag:
            if S3[0][j] == '#':
                S3flag = False
        if S4flag:
            if S4[0][j] == '#':
                S4flag = False
    if Tflag:
        T.pop(0)
    if Sflag:
        S.pop(0)
    if S2flag:
        S2.pop(0)
    if S3flag:
        S3.pop(0)
    if S4flag:
        S4.pop(0)

Tflag = True
Sflag = True
S2flag = True
S3flag = True
S4flag = True

for _ in range(N):
    for j in range(N):
        if Tflag:
            if T[-1][j] == '#':
                Tflag = False
        if Sflag:
            if S[-1][j] == '#':
                Sflag = False
        if S2flag:
            if S2[-1][j] == '#':
                S2flag = False
        if S3flag:
            if S3[-1][j] == '#':
                S3flag = False
        if S4flag:
            if S4[-1][j] == '#':
                S4flag = False
    if Tflag:
        T.pop(-1)
    if Sflag:
        S.pop(-1)
    if S2flag:
        S2.pop(-1)
    if S3flag:
        S3.pop(-1)
    if S4flag:
        S4.pop(-1)

Tflag = True
Sflag = True
S2flag = True
S3flag = True
S4flag = True

for _ in range(N):
    for j in range(len(T)):
        if T[j][0] == '#':
            Tflag = False
    if Tflag:
        for i in range(len(T)):
            T[i].pop(0)

    for j in range(len(S)):
        if S[j][0] == '#':
            Sflag = False
    if Sflag:
        for i in range(len(S)):
            S[i].pop(0)

    for j in range(len(S2)):
        if S2[j][0] == '#':
            S2flag = False
    if S2flag:
        for i in range(len(S2)):
            S2[i].pop(0)

    for j in range(len(S3)):
        if S3[j][0] == '#':
            S3flag = False
    if S3flag:
        for i in range(len(S3)):
            S3[i].pop(0)

    for j in range(len(S4)):
        if S4[j][0] == '#':
            S4flag = False
    if S4flag:
        for i in range(len(S3)):
            S4[i].pop(0)

Tflag = True
Sflag = True
S2flag = True
S3flag = True
S4flag = True

for _ in range(N):
    for j in range(len(T)):
        if T[j][-1] == '#':
            Tflag = False
    if Tflag:
        for i in range(len(T)):
            T[i].pop(-1)

    for j in range(len(S)):
        if S[j][-1] == '#':
            Sflag = False
    if Sflag:
        for i in range(len(S)):
            S[i].pop(-1)

    for j in range(len(S2)):
        if S2[j][-1] == '#':
            S2flag = False
    if S2flag:
        for i in range(len(S2)):
            S2[i].pop(-1)

    for j in range(len(S3)):
        if S3[j][-1] == '#':
            S3flag = False
    if S3flag:
        for i in range(len(S3)):
            S3[i].pop(-1)

    for j in range(len(S4)):
        if S4[j][-1] == '#':
            S4flag = False
    if S4flag:
        for i in range(len(S3)):
            S4[i].pop(-1)

if S == T or S2 == T or S3 == T or S4 == T:
    print("Yes")
else:
    print("No")
