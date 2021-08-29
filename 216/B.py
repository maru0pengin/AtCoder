
N = int(input())
A = []
#リストAにappend()を使って格納していく
for _ in range(N):
    A.append(input())

def has_duplicates(seq):
    return len(seq) != len(set(seq))

if has_duplicates(A):
  print('Yes')
else :
  print('No')


# A_dic = {}

# for i in range(N):
#   A_dic[i]= A[i]

# A_dic_sorted = sorted(A_dic.items(), key=lambda x:x[1])
# print(A_dic_sorted[len(A_dic_sorted)-2][0]+1)
