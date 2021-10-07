X = list(input())
N = int(input())
S = []

maxLen = -1
for _ in range(N):
    inPut = input()
    maxLen = max(len(inPut), maxLen)
    S.append(list(inPut))

print(S)

print(maxLen)

for i in range(N-1):
    if X.index(S[i][0]) > X.index(S[i+1][0]):
        tem = S[i]
        S[i] = S[i+1]
        S[i+1] = tem


print(S)
