N,M = map(int,input().split())
g = [[] for _ in range(N+1)]
for _ in range(M):
  A,B = map(int,input().split())
  g[A].append(B)

print(g)

result = 0

# #始まりと終わりが同じ場合
# result += N

# #1本だけ道を通る場合
# result += M

for i in range(1,M+1):
  if  not(g[i] is None):
    result += 1
    num = g[i][0]
    if not(g[num] is None):
      result += 1
      num = g[num][0]
      if not(g[num] is None):
        result += 1
print(result)