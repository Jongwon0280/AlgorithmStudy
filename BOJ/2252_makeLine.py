import sys
from collections import deque
input = sys.stdin.readline

n,e = map(int,input().split())

maps = [[] for _ in range(n+1)]
degree = [0] * (n+1)

for i in range(e):
    stt,end = map(int,input().split())
    maps[stt].append(end)


# 진입차수 구하기.

for i in range(n+1):
    for j in maps[i]:
        degree[j]+=1


deq = deque([])

for i in range(1,n+1):
    if degree[i] == 0:
        deq.append(i)


while deq :
    node=deq.popleft()
    print(node,end=' ')

    for i in maps[node]:
        degree[i]-=1
        if degree[i] ==0 :
            deq.append(i)

        
        
    
