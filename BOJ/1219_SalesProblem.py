import sys
input = sys.stdin.readline

#시작노드는 0번 노드이다.

n,starter,ender,m = map(int,input().split())

line = []

dist=[-sys.maxsize]*(n+1)

for i in range(m):
    s,e,w = map(int,input().split())

    line.append([s,e,w])

value=list(map(int,input().split()))

# value는 노드를 방문했을때 얻는 값입니다.

dist[starter] =value[starter]


for i in range(n+100):
    for j in range(m):
        pnode=line[j]
        start = pnode[0]
        end = pnode[1]
        weight = pnode[2]
        

        if dist[start]== -sys.maxsize :
            continue
        elif dist[start] == sys.maxsize:
            dist[end]=sys.maxsize
        elif dist[end]<dist[start]+value[end]-weight:
            if i >n-1:
                dist[end]=sys.maxsize
            else :
                dist[end]=dist[start]+value[end]-weight
                
            
            


if dist[ender] == sys.maxsize :
    print("Gee")
elif dist[ender] == -sys.maxsize:
    print("gg")
else :
    print(dist[ender])



    
