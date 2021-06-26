n = int(input())
list = list(map(int,input().split()))

count = 0
flag = 0
while 1:
  for i in range(len(list)):
    if (list[i] % 2) == 0:
      list[i] = list[i]/2
    else:
      flag = 1
      break
  if flag == 1:
    break
  count += 1

print(count)
