
import sys
input = sys.stdin.readline
ls=[]
n, m = map(int,input().split())
ls=list(map(int,input().split()))
sum=0
max=0
for i in range(n):
    if max < ls[i]:
        max = ls[i]
    sum+=ls[i]

left=max
right=sum
value =0
while left<=right:
    mid = int((left+right)/2)
    sum=0
    count=0

    for i in range(n):
        if sum+ls[i]>mid:
            count+=1
            sum=0
        sum+=ls[i]

    if sum!=0 :
        count+=1
    if count > m :
        left=mid+1
    else:
        right=mid-1
        
print(left)
