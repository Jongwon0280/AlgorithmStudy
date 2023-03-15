n = int(input())
k=int(input())
ls=[]
start=1
end =k

while start <= end:
    mid = int((start+end)/2)
    cnt=0
    for i in range(1,n+1,1):
        if int(mid/i) >n:
            cnt+=n
        else :
            cnt+=int(mid/n)
    if cnt < k:
        start=mid+1
    else :
        end=mid-1
print(start)
