def getDigit(num):
    result = 1
    for i in range(num):
        result *= 10

    return result


N = list(input())
N.sort(reverse=True)
n = int(N[0])
# print(type(N[0]))
for i in range(1, len(N)):
    n = n*10 + int(N[i])

# print(n)
N = str(n)

a = int(N[0])
b = int(N[1])


n = int(N) % getDigit(len(N)-2)
# print(getDigit(len(N)-2))
n = str(n)
# print(n)
for i in range(len(N)-2):
    if len(str(a)) > len(str(b)):
        b = b*10 + int(n[0])
        n = int(n) % getDigit(len(n)-1)
        n = str(n)
        # print("test1")
    elif len(str(b)) > len(str(a)):
        a = a*10 + int(n[0])
        n = int(n) % getDigit(len(n)-1)
        n = str(n)
        # print("test2")
    elif len(str(b)) == len(str(a)):
        if a >= b:
            b = b*10 + int(n[0])
            n = int(n) % getDigit(len(n)-1)
            n = str(n)
            # print("test3")
        elif b > a:
            a = a*10 + int(n[0])
            n = int(n) % getDigit(len(n)-1)
            n = str(n)
            # print("test4")

    if (len(str(a)) + len(str(b)) == len(N)):
        break
print(a*b)
