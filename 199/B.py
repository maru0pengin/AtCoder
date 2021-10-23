N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


result = 0
flag = True
for i in range(1, 1001):
    for j in range(N):
        if not (A[j] <= i and i <= B[j]):
            flag = False
    if flag:
        result += 1
    flag = True
print(result)
