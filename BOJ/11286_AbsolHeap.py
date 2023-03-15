import heapq
import math
import sys
from heapq import heappush, heappop

heap=[]
n = int(input())

for i in range(n):
    num = int(sys.stdin.readline())
    if num!=0:
        ab = abs(num)
        heappush(heap,(ab,num))
    else :
        if heap:
            print(heappop(heap)[1],end="\n")
        else :
            print("0",end="\n")
