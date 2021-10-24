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
            # print("hoge")
            if A[i]-1 >= N:
                a = A[i]-1 - N
            else:
                a = A[i]-1 + N
            if B[i]-1 >= N:
                b = B[i]-1 - N
            else:
                b = B[i]-1 + N
            S[a], S[b] = S[b], S[a]

        else:
            S[A[i]-1], S[B[i]-1] = S[B[i]-1], S[A[i]-1]
    else:
        flag = not flag
    # print(S)

if flag:
    S[:N], S[N:] = S[N:], S[:N]

s = ''.join(S)
print(s)
