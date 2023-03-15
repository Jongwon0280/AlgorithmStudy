import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

even = 0

ans = True 

n = int(input())

def dfs(n):
    global even, ans
    visited[n]=1
    for i in maps[n]:
        
        if not visited[i]:
            evens[i]=(evens[n]+1)%2
     
            dfs(i)
            
            
        elif evens[n]==evens[i] :
            ans=False

for i in range(n):
    
    node , edge = map(int,input().split())

    maps=[[] for _ in range(node+1)]

    visited = [0] * (node+1)

    evens = [0]*(node+1)

    ans=True
    
    for j in range(edge):

        a ,b = map(int,input().split())
        maps[a].append(b)
        maps[b].append(a)
        
    for k in range(1,node+1,1):
        

        if ans :

            dfs(k)
        else :
            break
            
    if ans==False:
        print("NO")
    else :
        print("YES")
        

    
        
