import sys

from collections import deque

input = sys.stdin.readline

n ,m = map(int,input().split())

maps=[[] for _ in range(n+1)]

ans=[]

visited=[0]*(n+1)


def bfs(pnode,deq):
    global visited, maps

    deq.append([pnode,0])
    visited[pnode]=1
    sum=0

    while deq:
        node=deq.popleft()
        pr=node[0]
        weight = node[1]
        sum+=weight
        

        for index in maps[pr]:
            if not visited[index]:
                deq.append([index,weight+1])
                visited[index]=1
        
            
    return sum
    



for i in range(m):
    s,e=map(int,input().split())
    maps[s].append(e)
    maps[e].append(s)





for i in range(1,n+1):
    deq=deque([])
    ans.append(bfs(i,deq))
    visited=[0]*(n+1)

minval = sys.maxsize
answer = 0

for i in range(n):
    if minval>ans[i]:
        minval=ans[i]
        answer = i+1
print(answer)
        
    
    
    
    
