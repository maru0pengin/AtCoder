
#subject = ['a','b','c']
subject = ['c','h','o','k','u','d','a','i']
s = list(input())
result = [[ 0 for i in range(len(s)+1)] for j in range(len(subject))]
result.insert(0,[1 for i in range(len(s))])
# print(result)
# print(range(1,len(s)))
mod = 1000000007
for i in range(1,len(s)+1):
  for j in range(1,len(subject)+1):
    # print("s[i]:", s[i-1])
    # print("subject[j-1]:", subject[j-1])
    if s[i-1] == subject[j-1]:
      # print("i:", i)
      # print("j:", j)
      # print(result[j-1][i-1])
      result[j][i] = (result[j][i-1] + result[j-1][i-1]) % mod
    else:
      result[j][i] = result[j][i-1]
#print(result)
print(result[len(subject)][len(s)])
#abcababc
