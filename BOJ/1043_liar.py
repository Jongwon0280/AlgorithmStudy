import sys
#sys.setrecursionlimit(10000)
input = sys.stdin.readline
cnt=0
n,p = map(int,input().split())
parent = [0]*(n+1)
tp = list(map(int,input().split()))

def union(a,b):
    pa=find(a)
    pb = find(b)
    if pa > pb :
        parent[pa] = pb
    else :
        parent[pb] = pa

def find(a):

    if parent[a]==a:
        return a
    else :
        parent[a]=find(parent[a])
        return parent[a]


partyInfo = [[] for _ in range(p+1)]

for i in range(p):
    partyInfo[i]=list(map(int,input().split()))


for i in range(n+1):
    parent[i] = i

for i in range(p):
    if partyInfo[i][0] != 0 :
        prnode=partyInfo[i][1]
    
        for j in range(1,len(partyInfo[i])):
            comnode = partyInfo[i][j]
            union(prnode, comnode)

for i in range(p):
    connect =0
    if partyInfo[i][0] !=0 :
        
        prnode=partyInfo[i][1]
        for t in range(1,len(tp)):
            if find(prnode) == find(tp[t]):
                connect =1
                break
    if connect==0:
        cnt+=1
print(cnt)
        
            
    
