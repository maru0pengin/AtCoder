# # N,M = map(int,input().split())
# # g = [[] for _ in range(N+1)]
# # for _ in range(M):
# #   A,B = map(int,input().split())
# #   g[A].append(B)

# # print(g)

# # result = 0

# # # #始まりと終わりが同じ場合
# # # result += N

# # # #1本だけ道を通る場合
# # # result += M

# # for i in range(1,M+1):
# #   if  not(g[i] is None):
# #     result += 1
# #     num = g[i][0]
# #     if not(g[num] is None):
# #       result += 1
# #       num = g[num][0]
# #       if not(g[num] is None):
# #         result += 1
# # print(result)

# import sys
# sys.setrecursionlimit(10**7)

# N,M = map(int,input().split())
# graph = [-1 for _ in range(M)]

# for i in range(M):
#   A,B = map(int,input().split())
#   graph[A-1]= B-1

# def dfs(v):
#   if temp[v]:return
#   temp[v] = True
#   if len(graph)>0 and not graph[v] == -1:
#     dfs(graph[v])

# ans = 0
# for i in range(N):
#   temp = [False]*N
#   dfs(i)
#   ans += sum(temp)

# print(ans)
  # おまじない
import sys
sys.setrecursionlimit(10000)

# 入力の読み込み
N,M=map(int,input().split())
G=[[] for i in range(N)]
# G[i] は都市iから道路で直接繋がっている都市のリスト
for i in range(M):
  A,B=map(int,input().split())
  G[A-1].append(B-1)

# dfs
def dfs(v):
  if temp[v]: return  # 同じ頂点を2度以上調べないためのreturn
  temp[v]=True
  for vv in G[v]: dfs(vv)

ans=0

# 都市iからスタートする場合
for i in range(N):
	temp=[False]*N
	# temp[j] は都市jに到達可能かどうかを表す
	dfs(i)
	ans+=sum(temp)

print(ans)
