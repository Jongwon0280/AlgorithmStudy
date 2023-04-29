import sys
input =sys.stdin.readline

n = int(input())

parent = [0]*(n+1)
visited=[0]*(n+1)
maps= [[] for _ in range(n+1)]


def dfs(n):
    global maps,parent,visited
   
    visited[n]=1

    for node in maps[n]:
        if not visited[node]:
            parent[node]=n
            dfs(node)
    
    
    




for i in range(n-1):
    a,b=map(int,input().split())
    maps[a].append(b)
    maps[b].append(a)


dfs(1)

for i in range(2,n+1):
    print(parent[i])
