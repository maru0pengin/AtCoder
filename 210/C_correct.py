N, K = map(int, input().split())
c = list(input().split())

k = {}

for i in range(K):
  if c[i] in k:
    k[c[i]] += 1
  else:
    k[c[i]] = 1

result = len(k)
tem = len(k)

for  i in range(K,N):
  if c[i] in k:
    k[c[i]] += 1
  else:
    k[c[i]] = 1

  k[c[i-K]] -= 1
  if k[c[i-K]] == 0:
    k.pop(c[i-K])
  result = max(result, len(k))

print(result)

