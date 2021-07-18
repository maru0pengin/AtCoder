# import collections
# from collections import deque

# N, K = map(int, input().split())
# c = list(map(int, input().split()))

# k = deque([])
# max = 0
# tem = 0
# for  i in range(N):
#   if len(k) < K:
#     k.append(c[i])
#   else :
#     k.append(c[i])
#     k.popleft()
#   tem = len(set(k))
#   if tem > max:
#     max = tem

# print(max)


# import collections
# from collections import deque

# N, K = map(int, input().split())
# c = list(map(int, input().split()))

# k = deque(c[0:K])

# max = len(set(k))
# tem = len(set(k))

# for  i in range(K-1,N):
#   k.append(c[i])
#   k.popleft()
#   tem = len(set(k))
#   if tem > max:
#     max = tem

# print(max)






import collections
from collections import deque

N, K = map(int, input().split())
c = list(map(int, input().split()))

k = deque(c[0:K])

Max = len(set(c))
max = len(set(k))
tem = len(set(k))

for  i in range(K,N):
  if max == K or max == Max:
    break
  if not(c[i] in k):
    k.append(c[i])
    k.popleft()
    tem = len(set(k))
    if tem > max:
      max = tem
  else :
    k.append(c[i])
    k.popleft()


print(max)