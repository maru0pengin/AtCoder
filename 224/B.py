H, W = map(int, input().split())
A = []
for i in range(H):
    a = list(map(int, input().split()))
    A.append(a)

flag = True

for i1 in range(H):
    for i2 in range(i1, H):
        for j1 in range(W):
            for j2 in range(j1, W):
                if not (A[i1][j1] + A[i2][j2] <= A[i2][j1] + A[i1][j2]):
                    flag = False

if flag:
    print("Yes")
else:
    print("No")
