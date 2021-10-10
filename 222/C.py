# str1基準の判定
def judgment(str1, str2):
    if str1 == str2:
        return "draw"
    if str1 == "G":
        if str2 == "C":
            return "win"
        else:
            return "loss"
    if str1 == "P":
        if str2 == "G":
            return "win"
        else:
            return "loss"
    if str1 == "C":
        if str2 == "P":
            return "win"
        else:
            return "loss"


N, M = map(int, input().split())

A = []
for i in range(2*N):
    a = list(input())
    A.append([a, 2*N - (i+1), 0])
# print(A)


for j in range(M):
    i = 0
    while True:
        if judgment(A[i][0][j], A[i+1][0][j]) == "win":
            A[i][2] += 1
        elif judgment(A[i][0][j], A[i+1][0][j]) == "loss":
            A[i+1][2] += 1

        i += 2

        if i > len(A)-1:
            break
    A = sorted(
        A,
        key=lambda x: (x[2], x[1]),
        reverse=True
    )
    # print(A)

# A.sort(key=lambda x: x[2], reverse=True)

for a in A:
    print(2*N - a[1])

# print(A)
