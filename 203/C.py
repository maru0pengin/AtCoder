N, K = map(int, input().split())
g = []
for i in range(N):
    A, B = map(int, input().split())
    g.append([A, B])

g.sort()

for i in range(N):
    A, B = g[i]
    if K >= A:
        K += B
    else:
        break
print(K)
