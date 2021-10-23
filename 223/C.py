N = int(input())

AB = []
for _ in range(N):
    a, b = map(int, input().split())
    AB.append([a, b])


totalTime = 0
halfTime = 0

for ab in AB:
    totalTime += ab[0]/ab[1]
halfTime = totalTime/2

answer = 0
nowTime = 0

for i in range(N):
    nowTime += AB[i][0]/AB[i][1]
    if nowTime > halfTime:
        nowTime -= AB[i][0]/AB[i][1]
        subTime = halfTime - nowTime
        answer += subTime*AB[i][1]
        break
    else:
        answer += AB[i][0]


print(answer)
