import sys
from heapq import heappush, heappop
input = sys.stdin.readline


inf = sys.maxsize

n,m = map(int , input().split())

start = int(input())

maps = [[] for _ in range(n+1)]

dist = [inf]*(n+1)

visited = [0] * (n+1)

dist[start]= 0

for i in range(m):
    s,e,w = map(int, input().split())

    maps[s].append([e,w])


heap= []
heappush(heap,[0,start])


while heap :
    minnode=heappop(heap)
    if visited[minnode[1]]==1 :
        continue

    visited[minnode[1]]=1

    for  k in maps[minnode[1]]:
        if  dist[k[0]] > dist[minnode[1]]+k[1]:
            dist[k[0]]=dist[minnode[1]]+k[1]
            heappush(heap,[dist[k[0]],k[0]])



for i in range(1,len(dist)) :
    if visited[i] :
        
        print(dist[i])
    else :
        print("INF")            

    
    
