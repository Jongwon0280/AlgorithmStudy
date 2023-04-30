import sys

input = sys.stdin.readline

n,question = map(int,input().split())


    


treeSize=1
tmp=n
while tmp!=0:
    tmp=tmp//2
    treeSize *=2
treeSize=treeSize * 2


startIndex = treeSize//2

tree = [sys.maxsize] * (treeSize+1)

def change_node(a,value):
    global tree
    dif=value-tree[a]


    while a>0:
        
        tree[a]+=dif
        a=a//2

def find_min(start,end):
    global tree
    pmin=sys.maxsize
    while start<=end:
        if start %2==1:
            
            pmin=min(pmin,tree[start])
            start+=1
        if end %2==0:
            
            pmin=min(pmin,tree[end])
            end-=1
        start=start//2
        end = end//2
    return pmin
            

        

for i in range(n):
    tree[startIndex+i]=int(input())

i=treeSize


while i != 1:
    tree[i//2]=min(tree[i//2],tree[i])
    i=i-1


for i in range(question):
    a , b = map(int,input().split())
    a=a+startIndex-1
    b=b+startIndex-1
    print(find_min(a,b))



        

    
