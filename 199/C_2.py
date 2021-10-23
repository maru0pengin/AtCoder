N = int(input())
S = list(input())
Q = int(input())

tab = [map(int, input().split()) for _ in range(Q)]
T, A, B = [list(i) for i in zip(*tab)]

flag = False

for i in range(Q):
    a = 0
    b = 0
    if T[i] == 1:
        if flag:
            if A[i]-1 > N:
                a = A[i]-1 - N
            else:
                a = A[i]

            else:
            S[A[i]-1], S[B[i]-1] = S[B[i]-1], S[A[i]-1]
    else:
        S1, S2 = S2, S1

s = ''.join(S)
print(s)
