import sys
import heapq
from heapq import heappush , heappop
from queue import PriorityQueue
input = sys.stdin.readline
pq=PriorityQueue()
ls = []
sum=0
n = int(input())
for i in range(n):
    date=int(input())
    pq.put(date)
a=0
b=0

while pq.qsize()>0:
    
    if sum ==0:
        sum+=pq.get()
        sum+=pq.get()
        pq.put(sum)
    else:
        
        sum+=pq.get()
        
        
    
print(sum)
    
