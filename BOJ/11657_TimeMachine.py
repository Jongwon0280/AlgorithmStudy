import sys
input = sys.stdin.readline

n,m = map(int ,input().split())

dist=[sys.maxsize]*(n+1)

line = []

for i in range(m):
    s,e,w = map(int,input().split())
    line.append([s,e,w])

    
dist[1]=0
# start node is number 1

# 벨만포드는 간단하다 . 시작점을 제외시킨후 노드들의 경로를 조사하면
# 모든 경로값이 최단으로 나올 수 있다.
# 물론 사이클이 존재하면 안된다.

for i in range(n):
    for j in range(m):
        pnode=line[j]
        start = pnode[0]
        end = pnode[1]
        weight = pnode[2]

        if dist[start]!= sys.maxsize and dist[end] > dist[start]+weight:
            dist[end] = dist[start]+weight


# 사이클 존재유무는 n-1번 루프 수행 후, 확인해준다.

cycle = False

for i in range(m):
    
    pnode=line[i]
    start = pnode[0]
    end = pnode[1]
    weight = pnode[2]

    if dist[start]!= sys.maxsize and dist[end] > dist[start]+weight:
        cycle = True
        break
            

if cycle:
    print("-1")
else :
    for i in range(2,n+1):
        if dist[i]!=sys.maxsize:
            print(dist[i])
        else:
            print("-1")
    
    
            
        

