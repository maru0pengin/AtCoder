N = int(input())
A = list(map(int, input().split()))

A_dic = {}

for i in range(N):
  A_dic[i]= A[i]

A_dic_sorted = sorted(A_dic.items(), key=lambda x:x[1])
print(A_dic_sorted[len(A_dic_sorted)-2][0]+1)
