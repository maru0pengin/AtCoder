n = int(input())

N = n

result = []

while N > 0:
  if N % 2 == 0:
    result.append('B')
    N = N /2
  else:
    result.append('A')
    N = N - 1
    
if len(result) <=120:
  for e in reversed(result):
    print(e, end='')
  print('')