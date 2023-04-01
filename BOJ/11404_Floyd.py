import sys
input = sys.stdin.readline

n = int(input())

m = int(input())

dist = [[sys.maxsize]*(n+1) for _ in range(n+1)]



for i in range(m):
    s,e,w = map(int,input().split())
    if dist[s][e] > w :
        dist[s][e] =w

for i in range(1,n+1):
    dist[i][i] = 0


for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if dist[i][j] > dist[i][k]+dist[k][j]:
                dist[i][j] = dist[i][k]+dist[k][j]


for i in range(1,n+1):
    for j in range(1,n+1):
        if dist[i][j] == sys.maxsize :
            print(0,end=" ")
        else :
            print(dist[i][j],end=" ")
    print()
        
