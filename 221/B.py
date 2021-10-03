
S = input()
T = input()

if S == T:
    print("Yes")
else:
    strS = list(S)
    strT = list(T)
    for i in range(len(strS)):
        if not(strS[i] == strT[i]) and i < len(strS):
            if strS[i] == strT[i+1] and strS[i+1] == strT[i]:
                print("Yes")
                flag = 1
                break
            else:
                print("No")
                break


# count = 1
# a = A % 10
# A = A//10
# while True:
#     a += (A % 10) * count * K
#     A = A // 10

#     if A == 0:
#         break

#     count *= K


# count = 1
# b = B % 10
# B = B//10
# while True:
#     b += (B % 10) * count * K
#     B = B // 10

#     if B == 0:
#         break

#     count *= K

# print(a * b)
