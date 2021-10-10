N, P = map(int, input().split())
a = list(map(int, input().split()))

count = 0
for num in a:
    if num < P:
        count += 1

print(count)
