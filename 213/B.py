N = int(input())
A = list(map(int, input().split()))

A_dic = {}

for i in range(len(A)):
  A_dic[i]= A[i]

#print(A_dic)

#A.sort()
A_dic_sorted = sorted(A_dic.items(), key=lambda x:x[1])

#print(A_dic_sorted)

print(A_dic_sorted[len(A_dic_sorted)-2][0]+1)
