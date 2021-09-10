# L,Q = map(int,input().split())
# cx = [map(int, input().split()) for _ in range(Q)]
# c, x = [list(i) for i in zip(*cx)]

# wood = [L]
# for i in range(Q):
#   if c[i] == 1:
#     sum = 0
#     for j in range(len(wood)):
#       sum += wood[j]
#       if sum >= x[i]:
#         sum -= wood[j]
#         w = wood.pop(j)
#         wood.insert(j,x[i]-sum)
#         wood.insert(j+1,w-(x[i]-sum))
#         break
#   if c[i] == 2:
#     sum = 0
#     for w in wood:
#       sum += w
#       if sum >= x[i]:
#         print(w)
#         break


L,Q = map(int,input().split())
cx = [map(int, input().split()) for _ in range(Q)]
c, x = [list(i) for i in zip(*cx)]

wood = {L:L}

for i in range(Q):
  if c[i] == 1:
    sum = 0
    for j in range(len(wood)):
      
      sum += wood[j]
      if sum >= x[i]:
        sum -= wood[j]
        w = wood.pop(j)
        wood.insert(j,x[i]-sum)
        wood.insert(j+1,w-(x[i]-sum))
        break
  if c[i] == 2:
    sum = 0
    for w in wood:
      sum += w
      if sum >= x[i]:
        print(w)
        break