import sys
from collections import deque
input =sys.stdin.readline
n,li = map(int,input().split())
maps=[[] for _ in range(n+1)]

ans=[0]*(n+1)

def bfs(n):
    deq=deque()
    deq.append(n)
    visited[n]=1
    while deq :
        node=deq.popleft()
        for nex in maps[node]:
            if not visited[nex]:
                visited[nex]=1
                
                deq.append(nex)
                
                ans[nex]+=1
    
for i in range(li):
    a,b = map(int,input().split())
    
    maps[a].append(b)

for i in range(1,n+1):
    visited=[0]*(n+1)
    bfs(i)
maxi= 0

for i in range(1,n+1):
    maxi=max(maxi,ans[i])

for i in range(1,n+1) :
    if ans[i] ==maxi:
        print(i,end=' ')

