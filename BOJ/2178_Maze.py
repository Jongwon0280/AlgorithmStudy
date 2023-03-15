from collections import deque
import sys
input = sys.stdin.readline
def bfs(start,maps):
    q=deque([])
    q.append((0,0,start))
    visit[0][0]=1
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    while q:
        node=q.popleft()
        for i in range(4):
            
            nx = node[0]+dx[i]
            ny = node[1]+dy[i]
            value = node[2]+1
            
            if nx>=0 and nx<n and ny>=0 and ny<m :
                if not visit[nx][ny] and maps[nx][ny]:
                    visit[nx][ny]=1
                    maps[nx][ny]=value
                    q.append((nx,ny,value))
    print(maps[n-1][m-1])
    
    


n , m = map(int,input().split())
graph =[]
visit=[]
for i in range(n):
    graph.append(list(map(int,input().rstrip())))

for i in range(n):
    visit.append([0]*m)

bfs(1,graph)
