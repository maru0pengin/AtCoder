def dfs(node, past):
    v_in = [s for s in v if 1 in s and not past in s]
    if len(v_in) == 0:
        return
    else まだ途中なら:
    　　　　処理内容


M = int(input())
v = []
for _ in range(M):
    v1, v2 = map(int, input().split())
    v.append([v1, v2])
p = list(map(int, input().split()))

v_in = [s for s in v if 1 in s]

print(v_in)
