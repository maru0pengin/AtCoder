# N,K = map(int,input().split())

# g = {}

# for i in range(N):
#   A,B = map(int,input().split())
#   if A in g:
#     g[A].append(B)
#   else:
#     g[A] = [B]
# g = sorted(g.items())

# result = 0
# while True:
#   result += 1
#   K -= 1
#   if len(g) > 0:
#     if result == g[0][0]:
#       K += sum(g[0][1])
#       g.pop(0)
  
  
#   if len(g) == 0:
#     result += K
#     break

#   if K == 0:
#     break

# print(result)


# N,K = map(int,input().split())
# g = {}

# for i in range(N):
#   A,B = map(int,input().split())
#   if A in g:
#     g[A].append(B)
#   else:
#     g[A] = [B]
# g = sorted(g.items())
# print(g)
# result = 0


# while True:
#   result += 1
#   K -= 1 
#   print("result{0}".format(result))
#   print("g{0}".format(g))
#   if result == g[0][0]:
#     K += sum(g[0][1])
#     g.pop(0)
#     print(g)
#   else:
#     if g[0][0] <= K:
#       result += g[0][0]-1
#       K -= g[0][0]-1
#     else:
#       result += K-1
#       K = 1
#   if K == 0:
#     break
#   if len(g) == 0:
#     result += K
#     break


# print(result)



N,K = map(int,input().split())
g = {}

for i in range(N):
  A,B = map(int,input().split())
  if A in g:
    g[A].append(B)
  else:
    g[A] = [B]
g = sorted(g.items())
# print(g)
result = 0

for i in range(N):
  diff = g[0][0] - result
  result += diff
  K -= diff

  if K >= 0:
    K += sum(g[0][1])
    g.pop(0)
    if len(g) == 0:
      result += K
      break
  else:
    result += K
    break

print(result)

