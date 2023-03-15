from collections import deque

mydeq = deque()
result=[]
n,l = map(int,input().split())
an = list(map(int,input().split()))

for i in range(n):
    while mydeq and mydeq[-1][1]>an[i]:
        mydeq.pop()
    mydeq.append((i,an[i]))
    if mydeq[0][0]<=i-l:
        mydeq.popleft()
   
    result.append(mydeq[0][1])

for i in result:
    print(i,end=' ')
