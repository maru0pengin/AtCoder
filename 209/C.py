N = int(input())
C = list(map(int,input().split()))

C = sorted(C)

result = 1

for i in range(N) :
  result = result * (C[i]-i) %(10**9 + 7)

print(result)
