N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

result = 100000000000
tem = 0

n = 0
m = 0

while n < N and m < M:
  result = min(result,abs(A[n]-B[m]))

  if B[m] >= A[n] :
    n += 1
  else:
    m += 1

print(result)



# if N < M:
#   for i in range(N):
#     if N[i] < M
#     for j in range(M):
#       result = min(result,abs(A[i]-B[j]))
# print(result)
