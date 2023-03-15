import sys
input=sys.stdin.readline

def find(node):
    if node == parent[node]:
        return node
    else :
        parent[node] = find(parent[node])
        return parent[node]

def union(a,b):
    pa=find(a)
    pb=find(b)

    if pa > pb :
        parent[pb]=pa
    else :
        parent[pa]=pb
        


travel=[]

n = int(input())
m=int(input())

parent=[0]*(n+1)

for i in range(1,n+1):
    parent[i]=i
    

maps=[[] for _ in range(n+1)]
for i in range(1,n+1):
    maps[i]=[0]+list(map(int,input().split()))


travel =[0]+ list(map(int,input().split()))

for i in range(1,n+1):
    for j in range(1,n+1):
        if maps[i][j]==1:
            union(i,j)


cond=find(travel[1])
sig=1
for i in range(2,n+1):
    if find(travel[i])==cond:
        continue
    else :
        sig=0
        print("NO")

if sig==1 :
    print("YES")

            
