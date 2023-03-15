import math
n= int(input())

ls = [0]*10000001

for i in range(2,len(ls),1):
    ls[i]=i

for i in range(2,int(math.sqrt(len(ls)))+1,1):
    if ls[i]==0:
        continue
    else :
        for j in range(i+i,len(ls),i):
            ls[j]=0


for i in range(n,len(ls)+1,1):
    if ls[i]!=0:
        st=list(str(ls[i]))

        cnt=1
        start=0
        end=len(st)-1
        while start < end:
            if int(st[start])!=int(st[end]):
                cnt=0
                break
            start+=1
            end-=1
        if cnt==1:
            print(ls[i])
            break
                
