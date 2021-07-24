# s = list(input())

# result = []

# subject = ['c','h','o','k','u','d','a','i']
# subject = ['c','h',]

# for i in range(len(s)):
#   if s[i] == 'c':
#     result.append(['c'])
#   for j in range(1,len(subject)):
#     if s[i] == subject[j] :
#       for k in range(len(result)):
#         if result[k][-1] == subject[j]:
#           result.append(subject[0:j+1])
#         else:
#           result[k].append(subject[j])
#   print(result)
# count = 0

# for i in range(len(result)):
#   if result[i] == subject:
#     count +=1

# print(result)
# print(count)
# print(len(result))
# print(count % (10^9 + 7))






s = list(input())

c = 0
h = []
o = []
K = []
u = []
d = []
a = []
I = []

#subject = ['c','h','o','k','u','d','a','i']
subject = ['c','h','o','k']

for i in range(len(s)):
  if s[i] == 'c':
    c += 1
  if s[i] == 'h' :
    for k in range(c):
      if len(h) <= k:
        h.append(1)
      else:
        h[k] += 1
  if s[i] == 'o':
    for k in range(len(h)):
      for j in range(h[k]):
        if len(o) <= j:
          o.append(1)
        else:
          o[j] += 1
  if s[i] == 'k':
    for k in range(len(o)):
      for j in range(o[k]):
        if len(K) <= j:
          K.append(1)
        else:
          K[j] += 1
  if s[i] == 'u':
    for k in range(len(K)):
      for j in range(K[k]):
        if len(u) <= j:
          u.append(1)
        else:
          u[j] += 1
  if s[i] == 'd':
    for k in range(len(u)):
      for j in range(u[k]):
        if len(d) <= j:
          d.append(1)
        else:
          d[j] += 1
  if s[i] == 'a':
    for k in range(len(d)):
      for j in range(d[k]):
        if len(a) <= j:
          a.append(1)
        else:
          a[j] += 1

  if s[i] == 'i':
    for k in range(len(a)):
      for j in range(a[k]):
        if len(I) <= j:
          I.append(1)
        else:
          I[j] += 1

  #     if result[k][-1] == 'c':
  #       result[k].append('h')
  #     if result[k][-1] == 'h':
  #       result.append(['c','h+'])

  # if s[i] == 'o' :
  #   for k in range(len(result)):
  #     if result[k][-1] == 'o':
  #       result.append(['c','h','o+'])
  #     if result[k][-1] == 'h':
  #       result[k].append('o')

# count = 0

# for i in range(len(result)):
#   if result[i] == subject:
#     count +=1
# print(c)
# print(h)
# print(o)
# print(K)
# print(I)
count = 0

for i in range(len(I)):
  count += I[i]

print(count)
#print(count % (10^9 + 7))


