import sys
from heapq import heappop, heappush

input = sys.stdin.readline

inf = sys.maxsize



n,m,k = map(int ,input().split())

maps = [[] for _ in range(n+1)]

dist=[ [inf]*k for _ in range(n+1)]

for i in range(m):
    s,e,w = map(int,input().split())

    maps[s].append([e,w])

heap=[]

dist[1][0]=0


heappush(heap,[0,1])

while heap :
    pnode=heappop(heap)


    for nnode in maps[pnode[1]] :
        if dist[nnode[0]][k-1] > pnode[0]+nnode[1]:
            dist[nnode[0]][k-1] = pnode[0]+nnode[1]
            dist[nnode[0]].sort()
            heappush(heap, [pnode[0]+nnode[1],nnode[0]])


for i in range(1,n+1):
    if dist[i][k-1] == inf :
        print("-1")
    else :
        print(dist[i][k-1])
