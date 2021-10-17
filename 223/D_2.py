N, M = map(int, input().split())
AB = []
AB_all = []
for _ in range(M):
    a, b = map(int, input().split())
    if a > b:
        AB.append([a, b])
    AB_all.append([a, b])

    if [b, a] in AB_all:
        print(-1)
        exit()
AB.sort()

resultArray = []
j = 0
for i in range(1, N+1):
    if i == AB[j][1]:
        resultArray.append(AB[j][0])
        if j < len(AB)-1:
            j += 1
    resultArray.append(i)

resultArray = list(dict.fromkeys(resultArray))

for i in range(N):
    print(resultArray[i], end="")
    print(" ", end="")

print("")
