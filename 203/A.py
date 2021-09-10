import sys
a,b,c = input().split()

if a != b and a !=c and c != b:
  print(0)
else:
  if a == b :
    print(c)
    sys.exit()
  if a == c :
    print(b)
    sys.exit()
  if b == c:
    print(a)
    sys.exit

print(0)
# import sys
# list = list(map(int,input().split()))
# if len(set(list)) == 3:
#   print(0)
# else:
#   if list[0] == list[1] :
#     print(list[2])
#     sys.exit()
#   elif list[0] == list[2] :
#     print(list[1])
#     sys.exit()
#   elif list[1] == list[2]:
#     print(list[0])
#     sys.exit