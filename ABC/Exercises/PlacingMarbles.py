s = list(input())

s = map(int,s)

count = 0
for i in s:
  if i == 1:
    count += 1

print(count)
