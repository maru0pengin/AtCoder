X = list(input())

X = list(map(int, X))

count = 0

if X.count(X[0]) == 4:
  print("Weak")
else:
  for i in range(3):
    if X[i]+1 == X[i+1] or (X[i] == 9 and X[i+1] == 0):
      count += 1

  if count == 3:
    print("Weak")
  else:
    print("Strong")


#sys.exit(1) が効かない