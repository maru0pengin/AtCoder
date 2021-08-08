H, W, N = map(int, input().split())
AB = [map(int, input().split()) for _ in range(N)]
A, B = [list(i) for i in zip(*AB)]

A_dic = {}
B_dic = {}

for i in range(len(A)):
  A_dic[i]= A[i]
  B_dic[i]= B[i]

A_dic_sorted = sorted(A_dic.items(), key=lambda x:x[1])
B_dic_sorted = sorted(B_dic.items(), key=lambda x:x[1])

count = 0

for i in range(len(A_dic_sorted)):
  A[A_dic_sorted[i][0]] -= ((A_dic_sorted[i][1]-1) - count)
  count += 1

count = 0
for i in range(len(B_dic_sorted)):
  B[B_dic_sorted[i][0]] -= ((B_dic_sorted[i][1]-1) - count)
  count += 1

for i in range(len(A)):
  print(str(A[i]) +' '+ str(B[i]))
