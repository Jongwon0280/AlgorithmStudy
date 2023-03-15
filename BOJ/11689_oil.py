import math
n = int(input())
res = n

ls = [0]*(n+1)

for i in range(1,n+1):
    ls[i]=i




for key in range(2,int(math.sqrt(n))+1):
    if n % key ==0:
        res = res - int(res/key)
        while n % key ==0:
            n /=key


if n >1:
    res = res - int(res/n)
print(int(res))
