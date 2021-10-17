N = int(input())
A = list(map(int, input().split()))

A = [a % 200 for a in A]

A2 = list(set(A))
result = 0
for a2 in A2:
    X = A.count(a2)
    result += (X*(X-1))//2
print(result)
