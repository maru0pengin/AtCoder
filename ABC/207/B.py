import math
a,b,c,d = map(int,input().split())
blue = a
red = 0
i=0

if b>=d*c:
  print(-1)
else:
  print(math.ceil(a/(d*c-b)))

# else:
#   while True:
#     if(blue<=red*d):
#       print(i)
#       break
#     else:
#       blue = blue + b
#       red = red + c
#       i += 1
