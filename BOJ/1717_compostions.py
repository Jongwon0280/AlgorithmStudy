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

    if pa < pb :
        parent[b]=pa
    else :
        parent[a]=pb
        

n,m = map(int,input().split())

parent = [0]*(n+1)

for i in range(0,n+1):
    parent[i]=i

for i in range(m):
    op,a,b=map(int,input().split())
    
    #find
    if op==1:
        ta=find(a)
        tb=find(b)
        if ta==tb:
            print("YES")
        else :
            print("NO")
    #union
    else :
        union(a,b)
        
        

    
    

