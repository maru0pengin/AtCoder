N = int(input())
t = [0] * N
l = [0] * N
r = [0] * N

for i in range(N):
  t[i], l[i], r[i] = map(int, input().split())

  if t[i] == 2:
    r[i] += -0.5
  if t[i] == 3:
    l[i] += +0.5
  if t[i] == 4:
    l[i] += +0.5
    r[i] += -0.5

ans = 0
for i in range(N):
  for j in range(i+1,N):
    ans += (max(l[i],l[j]) <= min(r[i],r[j]))

print(ans)


# N = int(input())
# t = [0] * N
# l = [0] * N
# r = [0] * N
# for i in range(N):
#     #上から順番に代入していく
#     t[i], l[i], r[i] = map(int, input().split())

# sum = 0
# start = 0
# end = 0
# for i in range(N):
#   start = l[i]
#   end = r[i]

#   for j in range(i+1,N):
#     if start <= r[j]  :
#       sum += r[j] - start + 1
#     if end >= l[j]:
#       sum += end - l[j] + 1
#     if start >= l[j] and end <= r[j]:
#       sum += end - start +1   
#     if start < l[j] and end > r[j]:
#       sum += r[j]-l[j] 

# print(sum)





# sum = -1
# array = [10000000000000000000000000000000,0]
# for i in range(N):
#   #print(i)
#   #print(array[0])
#   if l[i] <= array[0]:
#     array[0] = l[i]
    
#     sum += 1
#   if r[i] >= array[1]:
#     array[1] = r[i]
#     sum += 1

# print(sum)
