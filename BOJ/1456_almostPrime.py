import math
a, b = map(int,input().split())

ls = [0]*10000001

for i in range(2,len(ls),1):
    ls[i]=i

for i in range(2,int(math.sqrt(len(ls)))+1,1):
    if ls[i]==0:
        continue
    else :
        for j in range(i+i,len(ls),i):
            ls[j]=0

cnt =0

for i in range(2,10000001):
    t = ls[i]
    if t!=0:
        while ls[i] <= b / t:
            if ls[i]>= a/t:
                cnt+=1
            t = t * ls[i]

print(cnt)
        
