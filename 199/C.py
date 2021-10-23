N = int(input())
S = list(input())
Q = int(input())

tab = [map(int, input().split()) for _ in range(Q)]
T, A, B = [list(i) for i in zip(*tab)]

# print(S)
# print(T)
# print(A)
# print(B)

for i in range(Q):
    if T[i] == 1:
        S[A[i]-1], S[B[i]-1] = S[B[i]-1], S[A[i]-1]
    else:
        S[:N], S[N:] = S[N:], S[:N]

s = ''.join(S)
print(s)
