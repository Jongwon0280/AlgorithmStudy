import sys
import heapq
from heapq import heappush, heappop

def union(a,b):
    global parent
    ca=find(a)
    cb =find(b)


    if ca>cb :
        parent[a]=cb
    elif ca < cb :
        parent[b]=ca
  

    
    


def find(node):
    global parent

    if parent[node] ==node:
        return node
    else :
        parent[node]=find(parent[node])
        return parent[node]
    
    


input = sys.stdin.readline


n,m = map(int,input().split())

parent=[-1]*(n+1)

for i in range(len(parent)):
    parent[i]=i


heap = []



for i in range(m):
    s,e,w = map(int, input().split())
    heappush(heap,[w,s,e])
ans =0

use=0

while use < n-1: 
    pnode=heappop(heap)
    

    a=find(pnode[1])
    b=find(pnode[2])
    if a!=b:
        
        union(pnode[1],pnode[2])
        ans+=pnode[0]
        use+=1
    

print(ans)
        
    




    
