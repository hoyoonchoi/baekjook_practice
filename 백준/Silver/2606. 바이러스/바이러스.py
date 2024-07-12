N=int(input())
M=int(input())

graph = [[0]*(N+1)for _ in range(N+1)]
for i in range (M):
    a,b = map(int,input().split())
    graph[a][b] = graph[b][a] =1 

#방문 리스트 행렬 
visited1 = [0]*(N+1)
visited2 = visited1.copy()

lst=[]
#dfs 함수 만들기
def dfs(V):
    visited1[V] = 1 
    lst.append(V)
    for i in range(1,N+1):
        if graph[V][i] == 1 and visited1[i] == 0:
            dfs(i)

   

dfs(1)
print(len(lst)-1)
