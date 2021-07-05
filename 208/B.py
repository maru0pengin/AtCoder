import math
P = int(input())

num = list(range(1,11))
num.reverse()

i = 0 
count = 0

while True:
  if i == 10:
    break
  if P >= math.factorial(num[i]):
    P = P - math.factorial(num[i])
    count += 1
  else:
    i += 1

print(count)

# a,b,c,d = map(int,input().split())
# blue = a
# red = 0
# i=0

# if b>=d*c:
#   print(-1)
# else:
#   print(math.ceil(a/(d*c-b)))

# else:
#   while True:
#     if(blue<=red*d):
#       print(i)
#       break
#     else:
#       blue = blue + b
#       red = red + c
#       i += 1
