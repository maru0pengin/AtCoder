N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()

D = [0 for i in range(N)]
for c in C:
    D[B[c-1]-1] += 1

result = 0
for a in A:
    result += D[a-1]

print(result)
