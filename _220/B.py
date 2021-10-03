K = int(input())
A, B = map(int, input().split())

count = 1
a = A % 10
A = A//10
while True:
    a += (A % 10) * count * K
    A = A // 10

    if A == 0:
        break

    count *= K


count = 1
b = B % 10
B = B//10
while True:
    b += (B % 10) * count * K
    B = B // 10

    if B == 0:
        break

    count *= K

print(a * b)
