def has_duplicates(seq):
    return len(seq) != len(set(seq))
S = []
for _ in range(4):
    S.append(input())

if has_duplicates(S):
  print("No")
else:
  print("Yes")
