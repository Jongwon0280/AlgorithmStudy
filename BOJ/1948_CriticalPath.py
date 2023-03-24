from collections import deque
import sys
import math

input = sys.stdin.readline

n = int(input())

m = int(input())

res1=0
visited=[0] * (n+1)
maps = [ [] for _ in range(n+1)]
rmaps = [ [] for _ in range(n+1)]


cpath = [0] * (n+1)

degree = [0] * (n+1)


for i in range(m):
    st,end,weight = map(int,input().split())

    maps[st].append([end, weight])
    rmaps[end].append([st, weight])
    degree[end]+=1
    


snode,enode = map(int,input().split())



deq=deque([])


for i in range(1,n+1) :
    
    if degree[i] ==0 :
        deq.append(i)

while deq :
    pnode = deq.popleft()

    
    for nnode in maps[pnode]:
        
        
        degree[nnode[0]]-=1
        cpath[nnode[0]]=max(cpath[nnode[0]] , cpath[pnode]+nnode[1])
        if degree[nnode[0]]==0:
                  
                  
                  
                  deq.append(nnode[0])
 


res1= cpath[enode]

deq=deque([])


cnt =0

deq.append(enode)
visited[enode]=1
while deq :
    pnode = deq.popleft()


    for nnode in rmaps[pnode]:
        
        if  cpath[pnode]-nnode[1] == cpath[nnode[0]]:
            
            cnt+=1
            if visited[nnode[0]] == 0 :
                
                visited[nnode[0]] =1
                deq.append(nnode[0])
                
                       
            
        

print(res1)
print(cnt)
        
        
        
