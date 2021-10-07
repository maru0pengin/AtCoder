S1 = input()
S2 = input()
S3 = input()
T = list(map(int, input()))


for t in T:
    if t == 1:
        print(S1, end='')
    if t == 2:
        print(S2, end='')
    if t == 3:
        print(S3, end='')

print('')
