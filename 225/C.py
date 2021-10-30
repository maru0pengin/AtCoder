N, M = map(int, input().split())
B = []
for _ in range(N):
    B.append(list(map(int, input().split())))


for n in range(N):
    for m in range(M):
        if m == 0:
            if not n == 0 and not (B[n-1][0] + 7 == B[n][0]):
                print("No")
                exit()
        elif not (B[n][m-1] + 1 == B[n][m]):
            print("No")
            exit()

        if B[n][m] % 7 == 0 and not m == M-1:
            print("No")
            exit()

print("Yes")
