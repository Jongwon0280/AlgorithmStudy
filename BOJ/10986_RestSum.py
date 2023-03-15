m, n = map(int,input().split())
num = list(map(int,input().split()))
sum=[0]*m
d=[0]*n
sum[0]=num[0]

cnt=0
for i in range(1,len(num)):
    sum[i]=sum[i-1]+num[i]
    
for i in range(0,len(sum)):
    sum[i]=sum[i]%n
    if sum[i] ==0:
        cnt+=1
    d[sum[i]]+=1
for i in d:
    if i != 0:
        cnt += ((i*(i-1))//2)

print(cnt)
    
