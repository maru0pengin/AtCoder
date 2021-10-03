A, B, C = map(int, input().split())

num = C
count = 1
while True:
    if num >= A and num <= B:
        print(num)
        break
    elif num > B:
        print(-1)
        break

    num = num * count
    count += 1
