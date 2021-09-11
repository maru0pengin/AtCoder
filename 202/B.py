S = list(input())
# print(S)

for i in range(len(S)):
    if S[i] == '6':
        S[i] = '9'
    elif S[i] == '9':
        S[i] = '6'

S.reverse()
# print(S)

for s in S:
    print(s, end='')
print('')
