import sys
import math
input = sys.stdin.readline
m,n = map(int,input().split())
ls=[0]*(n+1)
for i in range(2,n+1):
    ls[i]=i


for i in range(2,int(math.sqrt(n))+1):
    if ls[i] ==0:
        continue
    
        
    for j in range(i+i,n+1,i):
        ls[j]=0
            
            
    

for i in range(m,n+1):
    if ls[i] != 0 :
        print(ls[i])
