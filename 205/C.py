
# import math
# A,B,C = map(int,input().split())

# plusFlag = True

# powA = 0
# powB = 0

# count = 1
# while True:
#   if math.log(count, abs(A)) == C:
#     if C%2 != 0 and A<0:
#       powA = count * -1
#     else:
#       powA = count
#   if math.log(count, abs(B)) == C:
#     if C%2 != 0 and B<0:
#       powB = count * -1
#     else:
#       powB = count
#   if math.log(count, abs(A)) >= C and math.log(count, abs(B)) >= C:
#     break
#   count += 1

# if powA == powB:
#   print("=")
# if powA < powB:
#   print("<")
# if powA > powB:
#   print(">")



import math
A,B,C = map(int,input().split())

if C%2 == 0:
  if abs(A) == abs(B):
    print("=")
  if abs(A) < abs(B):
    print("<")
  if abs(A) > abs(B):
    print(">")
else:
  if A == B:
    print("=")
  if A < B:
    print("<")
  if A > B:
    print(">")
