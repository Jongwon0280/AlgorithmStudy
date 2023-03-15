import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
def dfs(cur,maps):
    
    if visited[cur]:
        return
    else :
        visited[cur]=1
        for i in maps[cur]:
            if not visited[i]:
                dfs(i,maps)
    



n,m=map(int,input().split())

visited=[0]*(n+1)
maps={}
for i in range(n):
    maps[i+1]=[]

for i in range(m):
    start,end=map(int,input().split())
    maps[start].append(end)
    maps[end].append(start)
cnt=0
for i in range(n):
    if not visited[i+1]:
        cnt+=1
        dfs(i+1,maps)
print(cnt)
    
