N, M = map(int, input().split())
AB = []
AB_all = []
for _ in range(M):
    a, b = map(int, input().split())

    if a > b:
        AB.append([a, b])
    AB_all.append([a, b])

    Boolean = [b, a] in AB_all
    if Boolean:
        print(-1)
        exit()

resultArray = []
for i in range(1, N+1):
    resultArray.append(i)

# print(AB)
# print(resultArray)

for i in range(len(AB)):
    resultArray.remove(AB[i][0])
    resultArray.insert(resultArray.index(AB[i][1]), AB[i][0])

# print(resultArray)

for i in range(N):
    print(resultArray[i], end="")
    print(" ", end="")
print("")
