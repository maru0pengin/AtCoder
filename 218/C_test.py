def rot(S):
    # print(S[::-1])
    # rint(*S[::-1])
    # print(zip(*S[::-1]))
    return list(zip(*S[::-1]))


def rot2(S):
    S = [s[::-1] for s in S]
    S = list(zip(*S))
    S = [list(s) for s in S]
    return S


S = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]

print(S)

S = rot2(S)
print(S)
