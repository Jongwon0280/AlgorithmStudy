import sys
sys.setrecursionlimit(10000)
arrive = False
def dfs(cur,depth):
    global arrive
   
    if visited[cur]:
        
        return
    else :
        if depth == 5:
            arrive=True
            return
            
        
        visited[cur]=1
        for i in maps[cur]:
            if not visited[i]:
                dfs(i,depth+1)
        visited[cur]=0
    



n,m=map(int,sys.stdin.readline().split())

visited=[0]*(n+1)
maps={}
for i in range(n):
    maps[i]=[]

for i in range(m):
    start,end=map(int,sys.stdin.readline().split())
    maps[start].append(end)
    maps[end].append(start)
for i in range(n):
    if arrive == True:
        break
    dfs(i,1)
    
if arrive :
    print(1)
else:
    print(0)
        

    
