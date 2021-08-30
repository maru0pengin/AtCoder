n = int(input())
N = n
result = []
while N > 0:
  if N % 2 == 0:
    result.append('B')
    N = N // 2
  else:
    result.append('A')
    N = N - 1

for e in reversed(result):
  print(e, end='')
print('')


# 人のコードを参考
# n = int(input())
# result = ""

# while True:
#   if n == 1:
#     result += "A"
#     break
#   if n%2 == 1:
#     n = n-1
#     result += "A"
#   else:
#     n = n//2
#     result += "B"

# print(result[::-1])
