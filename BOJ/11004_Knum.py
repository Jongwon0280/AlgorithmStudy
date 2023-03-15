import heapq
from heapq import heappop,heappush,heapify

answer=0
x,y = map(int,input().split())
ls=[]
ls=list(map(int,input().split()))
heapify(ls)

for i in range(y):
    answer=heappop(ls)
    
print(answer)
