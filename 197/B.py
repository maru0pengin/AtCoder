H, W, X, Y = map(int, input().split())

X = X-1
Y = Y-1
S = []

for _ in range(H):
    S.append(list(input()))


print(S)

result = 1

# 上
i = 1
while True:
    if X-i >= 0:
        if S[X-i][Y] == '.':
            result += 1
            i += 1
        else:
            break
    else:
        break


print(result)
# した
i = 1
while True:
    if X+i < H:
        if S[X+i][Y] == '.':
            result += 1
            i += 1
        else:
            break
    else:
        break

print(result)
#　右
i = 1
while True:
    if Y+i < W:
        if S[X][Y+i] == '.':
            result += 1
            i += 1
        else:
            break
    else:
        break
# 左

print(result)
i = 1
while True:
    if Y-i >= 0:
        if S[X][Y-i] == '.':
            result += 1
            i += 1
        else:
            break
    else:
        break

print(result)
