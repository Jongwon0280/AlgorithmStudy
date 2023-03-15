n=int(input())

count=1
sum=1
s,e = 1,1

while e<n:
    if sum ==n:
        e+=1
        sum+=e
        count+=1
        
    elif sum>n:
        sum-=s
        s+=1
    else :
        e+=1
        sum+=e
print(count)
        
