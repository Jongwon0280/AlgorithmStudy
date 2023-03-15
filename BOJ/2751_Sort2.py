import heapq
from heapq import heappop,heappush,heapify
import sys
input = sys.stdin.readline
n = int(input())
ls =[]

for i in range(n):
    ls.append(int(sys.stdin.readline()))

heapify(ls)

while ls :
    print(heappop(ls))



    
    
    
    
