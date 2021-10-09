X = list(input())
N = int(input())
S = []

maxLen = -1
for _ in range(N):
    inPut = input()
    maxLen = max(len(inPut), maxLen)
    S.append(list(inPut))

# print(S)

# print(maxLen)

for i in range(N):
    for j in range(len(S[i])):
        S[i][j] = X.index(S[i][j])

S.sort()

for i in range(N):
    for j in range(len(S[i])):
        S[i][j] = X[S[i][j]]

# print(S)

for i in range(N):
    for j in range(len(S[i])):
        print(S[i][j], end='')
    print('')
