S = list(input())
# print(S)
ListS = []

# print(S)
for i in range(len(S)):
    ListS.append(S)
    tem = S
    S = S[1:len(S)]
    S.append(tem[0])

ListS.sort()
# print(ListS)

for s in ListS[0]:
    print(s, end="")

print("")

for s in ListS[-1]:
    print(s, end="")

print("")
