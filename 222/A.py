N = list(input())


num = 4-len(N)
for _ in range(num):
    print("0", end="")

for n in N:
    print(n, end="")

print("")
