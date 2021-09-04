N = int(input())
p = list(map(int,input().split()))

q = [0 for _ in range(N)]
for i in range(1,N+1):
  q[p[i-1]-1] = i

for i in range(N):
  print(q[i],end='')
  print(' ',end='')

print('')