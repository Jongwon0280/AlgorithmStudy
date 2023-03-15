import sys
from collections import deque
input=sys.stdin.readline
a,b,c = map(int,input().split())
limits = [a,b,c]
visited=[[] for _ in range(200+1)]
for i in range(len(visited)):
    visited[i]=[0]*(200+1)
check=[0]*(200+1)

def bfs(a,b):

    deq=deque([])
    Sender=[0,1,2,0,1,2]
    Receive=[1,2,0,2,0,1]
    deq.append([0,0])
    visited[a][b]=1
    check[limits[2]]=1

    while deq:
        nownow=deq.popleft()
        A=nownow[0]
        B=nownow[1]
        C=limits[2]-A-B
    


        for index in range(6):

            now=[A,B,C]
            now[Receive[index]]+=now[Sender[index]]

        #넘쳤을때
            if now[Receive[index] ]>=limits [Receive[index]]:
                  now[Sender[index]]=now[Receive[index] ] -limits [Receive[index]] 

                  now[Receive[index] ]=limits[Receive[index] ] 
        #비워졌을때
            else:
                now[Sender[index]]=0

            if not visited[now[0]][now[1]] :
                visited[now[0]][now[1]]=1
                deq.append([now[0],now[1]])
            if now[0]==0:
                check[now[2]]=1



bfs(limits[0],limits[1])


for i in range(1,len(check)):
    if check[i]:
       print(i,end=" ")

