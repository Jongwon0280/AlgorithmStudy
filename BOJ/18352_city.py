import sys
from collections import deque
input = sys.stdin.readline


def bfs(s):
    qu = deque()
    qu.append(s)
    while qu :
        pr=qu.popleft()

        for ns in maps[pr]:
            
        
            if not visited[ns]:
                visited[ns]+=(visited[pr]+1)
                
                qu.append(ns)
                


n,nc,target,st = map(int,input().split())
visited = [0]*(n+1)

maps={}

for i in range(1,n+1):
    maps[i]=[]
    

for i in range(nc):
    a,b = map(int,input().split())
    
    maps[a].append(b)
   

bfs(st)
sig=0
for i in range(1,len(visited)):
    if visited[i] == target :
        sig=1
        
        print(i)

if not sig:
    print(-1)
