import math

N = int(input())

result = math.floor(1.08 * N)

if result < 206:
  print("Yay!")
elif result == 206:
  print("so-so")
elif result > 206:
  print(":(")