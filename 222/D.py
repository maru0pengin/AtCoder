N = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = 1
sabun = 1

for i in range(N):
    result *= ((b[i]-a[i] + 1) - 0)
    if not i == 0:
        sabun *= (b[i]-a[i] + 1) - (b[i-1]-a[i-1] + 1)

# print((result-sabun) % 998244353)
print((result))
print(sabun)
