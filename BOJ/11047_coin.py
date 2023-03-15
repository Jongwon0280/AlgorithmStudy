import sys
import heapq
from heapq import heappop , heappush
input=sys.stdin.readline
n,m = map(int,input().split())
ls =[]
for i in range(n):
    k=(int(input()))
    heappush(ls,((-1)*k,k))

length=len(ls)
cnt=0
for i in range(length):
    value=heappop(ls)[1]
    if value > m and m==0:
        break
    cnt+=int(m / value)
    m=m%value
    
    
print(cnt)
