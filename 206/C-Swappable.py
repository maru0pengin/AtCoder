import math
N = int(input())
A = list(map(int,input().split()))
num = []
total = 0

R = math.factorial(2)

def combinations_count(n):
    if n <= 1:
      return 0
    return math.factorial(n) // (math.factorial(n - 2) * R)

total = combinations_count(N)

for i in range(0,N-1):
  if not(A[i] in num):
    total -= combinations_count(A.count(A[i])) 
    num.append(A[i])
print(total)

# def combinations_count(n, r):
#     if n <= 1:
#       return 0
#     return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

# total = combinations_count(N,2)

# while True:
#   total -= combinations_count(A.count(A[0]),2) 
#   A = [x for x in A if x != A[0]]
#   print(A)
#   if len(A) == 0:
#     break

# print(total)




# for i in range(0,N):
#   for j in range(1,N-i):
#     if A[i] != A[i+j]:
#       count += 1
# for i in range(0,N-1):
#   for j in range(i+1,N):
#     if A[i] != A[j]:
#       count += 1
# for j in range(1,N):
#   for i in range(0,j):
#     if A[i] != A[j]:
#       count += 1