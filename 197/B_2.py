H, W, X, Y = map(int, input().split())
S = []
for _ in range(H):
    S.append(list(input()))

result = 1
X = X-1
Y = Y-1
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

for i in range(4):
    x = X
    y = Y
    while True:
        x += dx[i]
        y += dy[i]

        if x < 0 or y < 0 or x >= H or y >= W:
            break
        if S[x][y] == '#':
            break

        result += 1

print(result)
