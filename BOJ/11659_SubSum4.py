a,b=map(int,input().split())
numbers=list(map(int,input().split()))
sum=[0]*a
sum[0]=numbers[0]
result=[]
for i in range(1,a):
    sum[i]=sum[i-1]+numbers[i]

for i in range(b):
    s,e=map(int,input().split())
    if s==1 :
        result.append(sum[e-1])
    else :
        result.append(sum[e-1]-sum[s-2])

for i in result:
    print(i)
    
