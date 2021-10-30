N = list(input())


if N == N[::-1]:
    print("Yes")
    exit()

count = 0
i = 0
N2 = N[::-1]
while True:
    if N2[i] == '0':
        count += 1
        i += 1
    else:
        break


for _ in range(count):
    N.insert(0, '0')

if N == N[::-1]:
    print("Yes")
else:
    print("No")
