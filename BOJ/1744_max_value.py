import sys
import heapq
from heapq import heappush , heappop
from queue import PriorityQueue
plus = PriorityQueue()
minus = PriorityQueue()
input = sys.stdin.readline

sum=0
n = int(input())

for i in range(n):
    

    k=int(input())
    if k>0 :
        plus.put((-1)*k)
    else :
        minus.put(k)

while plus.qsize()>0 :
    if plus.qsize()==1:
        sum+=((-1)*plus.get())

    else :
        a=(-1)*plus.get()
        b=(-1)*plus.get()

        if a==1 or b==1 :
            sum+=(a+b)
        else :
            sum+=(a*b)

while minus.qsize()>0 :
    if minus.qsize()==1:
        sum+=(minus.get())

    else :
        a=minus.get()
        b=minus.get()
        sum+=(a*b)
print(sum)
        
        
        
        
        
        

