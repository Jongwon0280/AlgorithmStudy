import sys
input=sys.stdin.readline
from collections import deque

def dfs(s,maps,depth):
    global path
    if visited[s]:
        return
    else :

        print(s,end=' ')
        visited[s]=1
       
        
        for i in maps[s]:
            if not visited[i]:
                
                dfs(i,maps,depth+1)
            
        
def bfs(s,maps):
    quu=deque([])
    quu.append(s)
    visited[s]=1
    while quu:
        work=quu.popleft()
        print(work,end=' ')
        for i in maps[work]:
            if  not visited[i]:
                visited[i]=1
                quu.append(i)
            
        
        


n,m,s=map(int,input().split())
maps={}
path=[]
visited=[0]*(n+1)
for i in range(n):
    maps[i+1]=[]

for i in range(m):
    start,end = map(int,input().split())
    maps[start].append(end)
    maps[end].append(start)

for i in range(n):
    maps[i+1]=sorted(maps[i+1])

dfs(s,maps,1)
visited=[0]*(n+1)
print()

bfs(s,maps)
