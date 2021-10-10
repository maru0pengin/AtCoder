def rot(S):
    return list(zip(*S[::-1]))


N = int(input())
S = [input() for _ in range(N)]
T = [input() for _ in range(N)]

print(S)
S = rot(S)
print(S)
S = rot(S)
print(S)
S = rot(S)
print(S)
S = rot(S)
#S = zip(*S[::-1])
# print(S[::-1])

# S = list(zip(*S[::-1]))

# print(list(zip(*S[::-1])))
