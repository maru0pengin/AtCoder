P = list(map(int, input().split()))

l = list('abcdefghijklmnopqrstuvwxyz')

for p in P:
    print(l[p-1], end='')
print('')
