x,y = map(int,input().split())

if x == y:
  print(x)
else:
  if (x == 0 or y == 0) and (x == 1 or y== 1):
    print('2')
  elif (x == 0 or y == 0) and (x == 2 or y== 2):
    print('1')
  elif (x == 1 or y == 1) and (x == 2 or y== 2):
    print('0')