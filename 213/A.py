A, B = map(int, input().split())

A_binary = []
B_binary = []
C_binary = []

while A!=0:
  A_binary.append(A%2)
  A = A // 2

#A_binary.reverse()

while B!=0:
  B_binary.append(B%2)
  B = B // 2

#B_binary.reverse()

if len(A_binary) > len(B_binary):
  for i in range(len(A_binary)-len(B_binary)):
    B_binary.append(0)
else:
  for i in range(len(B_binary)-len(A_binary)):
    A_binary.append(0)


# len = min(lne(A_binary),len(B_binary))

for i in range(len(A_binary)):
  if A_binary[i] == B_binary[i]:
    C_binary.append(0)
  else:
    C_binary.append(1)

#C_binary.reverse()

C = 0

for i in range(0,len(C_binary)):
  #print(2**i * C_binary[i])
  C += 2**i * C_binary[i]

# print(A_binary)
# print(B_binary)

C_binary.reverse()
#print(C_binary)
print(C)