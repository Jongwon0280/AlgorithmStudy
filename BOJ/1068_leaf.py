import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
ls=list(map(int,input().split()))
delnode = int(input())
maps=[[] for _ in range(n)]
visited=[0]*(n)
ans=0

def dfs(n):
    global visited,ans
    visited[n]=1
    cnt=0
    for node in maps[n]:
        if not visited[node] and delnode!=node:
            cnt+=1
            dfs(node)
    if cnt==0 :
        ans+=1
            

    
    
start=999
for i in range(0,n):
    if ls[i]==-1:
        start = i
        continue
    maps[ls[i]].append(i)
    maps[i].append(ls[i])


if delnode == start :
    print(ans)

dfs(0)

print(ans)
