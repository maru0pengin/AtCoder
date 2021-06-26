import math

N = int(input())
A = list(map(int,input().split()))
count = 0
for j in range(1,N):
  for i in range(0,j):
    if A[i] != A[j]:
      count += 1

print(count)
