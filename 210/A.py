A, B = map(int, input().split())

max = A*6
min = 1*A

if B <= max and B >= min:
  print("Yes")
else:
  print("No")