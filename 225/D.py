N, Q = map(int, input().split())
query = []
for _ in range(Q):
    query.append(list(map(int, input().split())))

train = [[0] * 2 for _ in range(N+1)]

for q in query:
    if q[0] == 1:
        x = q[1]
        y = q[2]
        train[x][1] = y
        train[y][0] = x

    if q[0] == 2:
        x = q[1]
        y = q[2]
        train[x][1] = 0
        train[y][0] = 0
    if q[0] == 3:
        x = q[1]
        while True:
            if train[x][0] == 0:
                break
            else:
                x = train[x][0]

        count = 1
        result = [x]
        while True:
            x = train[x][1]
            if x == 0:
                print("")
                break
            else:
                count += 1
                result.append(x)
        print(count, end="")
        print("")
        [print('{0} '.format(x), end="") for x in result]

print("")
