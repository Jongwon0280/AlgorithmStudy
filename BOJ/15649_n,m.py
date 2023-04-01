import sys
from collections import deque

n ,m = map(int,input().split())
visited=[0]*(n+1)
def dfs(num,depth):
    global n,m, visited
    if depth == (m+1):
        for i in num:
            print(i,end=" ")
        print()
    for value in range(1,n+1):
        if visited[value]:
            continue
        num.append(value)
        visited[value]=1
        dfs(num,depth+1)
        num.pop()
        visited[value]=0


num=deque([])

dfs(num,1)

    
    
            
