N = int(input())
A = list(map(int,input().split()))

result = 0
for a in A:
  if a > 10:
    result = result + (a - 10)

print(result)