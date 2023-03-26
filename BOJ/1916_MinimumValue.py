import sys
from heapq import heappop, heappush

input = sys.stdin.readline
inf = 1000000
n = int(input())

m = int(input())

dist=[inf]*(n+1)

visited=[0] * (n+1)

maps = [[] for _ in range(n+1)]

heap =[]

for i in range(m):
    s, e , w = map(int,input().split())
    maps[s].append([e,w])

start,end = map(int,input().split())



dist[start]=0

heappush(heap,[0,start])

while heap :
    pnode=heappop(heap)
    if visited[pnode[1]]:
        continue

    visited[pnode[1]] =1

    for nnode in maps[pnode[1]] :
        if dist[nnode[0]] > dist[pnode[1]]+nnode[1]:
            dist[nnode[0]] = dist[pnode[1]]+nnode[1]
            heappush(heap, [dist[nnode[0]],nnode[0]])

            

print(dist[end])


    
