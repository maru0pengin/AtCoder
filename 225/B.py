N = int(input())
ab = []

for _ in range(N-1):
    ab.append(list(input().split()))


ab0 = ab[0]
ab1 = ab[1]

num = 0

if ab0[0] == ab1[0]:
    num = ab0[0]
elif ab0[0] == ab1[1]:
    num = ab0[0]
elif ab0[1] == ab1[1]:
    num = ab0[1]
elif ab0[1] == ab1[0]:
    num = ab0[1]
else:
    print("No")
    exit()

for e in ab:
    if not e[0] == num and not e[1] == num:
        print("No")
        exit()
print("Yes")
