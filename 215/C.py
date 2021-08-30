import itertools
s,k = input().split()
s = sorted(list(s))
k = int(k)

sList = sorted(list(set(itertools.permutations(s))))

# print(sList)
for s in sList[k-1]:
  print(s,end="")
print("")
