N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

tMinIndex = T.index(min(T))

result1 = []
result1.append(T[tMinIndex])

if tMinIndex != N-1:
  for i in range(tMinIndex,N-1):
    if S[i]+result1[-1] <= T[i+1]:
      result1.append(S[i]+result1[-1])
    else:
      result1.append(T[i+1])

result2 = []

if tMinIndex != 0:
  if S[-1]+result1[-1] <= T[0]:
    result2.append(S[-1]+result1[-1] )
  else:
    result2.append(T[0])

  for i in range(tMinIndex-1):
    if S[i]+result2[-1] <= T[i+1]:
      result2.append(S[i]+result2[-1])
    else:
      result2.append(T[i+1])



for r in result2:
  print(r)
for r in result1:
  print(r)

