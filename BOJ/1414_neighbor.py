import heapq
import sys
from heapq import heappush, heappop
input=sys.stdin.readline


n = int(input())



parent = [n for n in range(0,n)]

sums=0

def find(a):
    global parent
    
    if parent[a]==a :
        return a
    else :
        parent[a]=find(parent[a])
        return parent[a]
def union(a,b):
    global parent
    ax=find(a)
    bx=find(b)
    if ax<bx :
        parent[bx]=ax
    else:
        parernt[ax]=bx

heap = []
for i in range(n):
    s = list(input())
    for j in range(n) :
        if s[j]=='0':
            
            s[j]=0
        else :    
            
            if ord('a')<=ord(s[j]) and ord(s[j])<=ord('z'):
                s[j]=ord(s[j])-96
                
            elif ord('A')<=ord(s[j]) and ord(s[j])<=ord('Z'):
                s[j] = ord(s[j])-38
            sums=sums+s[j]
            if i==j:
                continue
            heappush(heap,[s[j],i,j])
            
           
            
    
    

    

used = 0

cost=0

while used != n-1:
    pnode=heappop(heap)
    pa = find(pnode[1])
    pb = find(pnode[2])
    if pa != pb:
        union(pnode[1],pnode[2])
        used+=1
        cost+=pnode[0]

print(sums-cost)
        
        
    
   
