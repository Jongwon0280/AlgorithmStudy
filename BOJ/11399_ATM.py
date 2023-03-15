n = int(input())
ls=[]
answer=0
ls=list(map(int,input().split()))

for i in range(n):
    ls[i]=list((ls[i],i))
    
sorted_list = sorted(ls)
sum=0
for i in range(n):
    sum+=sorted_list[i][0]
    answer+=sum
print(answer)
