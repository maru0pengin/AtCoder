N = int(input())
A = list(map(int, input().split()))
X = int(input())

SUMA = sum(A)
num = X//SUMA

result = num * len(A)
count = 0
num = SUMA * num

while True:
    num += A[count]
    if num > X:
        print(result+1)
        break
    else:
        count += 1
        result += 1


# SUMA = sum(A)
# count = 1
# num = SUMA
# while True:
#     if X < num:
#         break
#     else:
#         num += SUMA
#         count += 1


# result = count * len(A)

# print(num)
# print(result)

# if num == X:
#     print(result)
# else:
#     A.reverse()

#     count = 0
#     while True:
#         print(result)
#         num -= A[count]
#         if num < X:
#             print(result+1)
#             break

#         result -= 1
