import sys
import heapq
from heapq import heappush , heappop

input = sys.stdin.readline
start=0
cnt=0
n = int(input())
ls=[]
for i in range(n):
    l,k=map(int,input().split())
    heappush(ls,(k,l))
for i in range(n):
    node=heappop(ls)
    if node[1]>=start:
        cnt+=1
        start=node[0]
print(cnt)
    
    
    
