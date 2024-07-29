'''import sys 

sys.setrecursionlimit(10**7)
n= int(input())
graph = [[]for _ in range(n+1)]
for i in range(n-1):
    u,v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)'''
#그래프를 만드는 방식이 참신 하네 잘 기억 해놓으면 쓸일이 많이 있을거 같아요 


import sys

sys.setrecursionlimit(10**9)
n = int(sys.stdin.readline())
lines = [[]for _ in range(n+1)]
for _ in range(n-1):
    a , b = map(int, sys.stdin.readline().split())
    lines[a].append(b)
    lines[b].append(a)
dp = [[0,0]for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

def dfs(r):
    visited[r] =1
    dp[r][0] =1
    for i in lines[r]:
        if not visited[i]:
            dfs(i)
            dp[r][0] += min(dp[i][0], dp[i][1])
            dp[r][1] += dp[i][0]

dfs(1)
print(min(dp[1][0],dp[1][1]))