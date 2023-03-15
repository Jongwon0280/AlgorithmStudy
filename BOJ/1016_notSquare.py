import math
min,max = map(int,input().split())

ls=[1]*((max-min)+1)
cnt=0
for i in range(2,int(math.sqrt(max))+1):
    value = i * i
    index = int(min / value) #제곱수를 시작점에 맞추기 위함.
    if min % value !=0 : #나누어 떨어지지 않기 때문에 *value를 한번 해야함.
        index+=1

    for k in range(index,int(max/value)+1):
   
        ls[(k*value)-min]=0

for i in ls:
    if i==1:
        cnt+=1

print(cnt)
