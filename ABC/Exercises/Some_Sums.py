N, A, B = map(int, open(0).read().split())

count = 0
for i in range(N+1):
  sum = 0
  s = str(i)
  for j in range(1,len(s)+1):
    sum += int(s[-j])

  if A<=sum and sum<=B:
    count += i

print(count)