import sys
import math
from collections import deque
input = sys.stdin.readline

n = int(input())

work = [0]*(n+1)

ans = [0] * (n+1)

deg = [0] * (n+1)

maps = [[] for _ in range(n+1)]

for i in range(1,n+1):
    tmp=list(map(int,input().split()))
    
    tmp.remove(-1)
    work[i]=tmp.pop(0)

    for j in tmp :
        maps[j].append(i)
        deg[i]+=1



deq=deque([])

for i in range(1,len(deg)):
    if deg[i] == 0:
        deq.append(i)


while deq :
    node = deq.popleft()

    for j in maps[node]:

        ans[j]=max(ans[j] , ans[node]+work[node])
        deg[j]-=1

        if deg[j]==0 :
            deq.append(j)
        
        
for i in range(1,len(ans)):
    ans[i] +=work[i]
    print(ans[i])


        

    
    
