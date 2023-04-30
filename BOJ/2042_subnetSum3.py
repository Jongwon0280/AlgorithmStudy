import sys

input = sys.stdin.readline

n,chnage,sum = map(int,input().split())


    


treeSize=1
tmp=n
while tmp!=0:
    tmp=tmp//2
    treeSize *=2
treeSize=treeSize * 2


startIndex = treeSize//2

tree = [0] * (treeSize+1)

def change_node(a,value):
    global tree
    dif=value-tree[a]


    while a>0:
        
        tree[a]+=dif
        a=a//2

def subnet_sum(start,end):
    global tree
    psum = 0
    while start<=end:
        if start %2==1:
            
            psum+=tree[start]
            start+=1
        if end %2==0:
            
            psum+=tree[end]
            end-=1
        start=start//2
        end = end//2
    return psum
            

        

for i in range(n):
    tree[startIndex+i]=int(input())

i=treeSize
while i != 1:
    tree[i//2]+=tree[i]
    i=i-1


for i in range(chnage+sum):
    t , a , b = map(int,input().split())

    if t ==1:
        a=a+startIndex-1
        change_node(a,b)
    if t ==2:
        a=a+startIndex-1
        b=b+startIndex-1
        print(subnet_sum(a,b))

    
