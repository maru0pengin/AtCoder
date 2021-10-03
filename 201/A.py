A = list(map(int, input().split()))
A.sort()

# print(A)

if A[0] - A[1] == A[1] - A[2]:
    print("Yes")
else:
    print("No")
