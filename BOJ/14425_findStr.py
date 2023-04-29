import sys
input = sys.stdin.readline

n,m=map(int,input().split())

slist = []
ans=0
for i in range(n):
    s = input()
    slist.append(s)

for i in range(m):
    s = input()
    if s in slist:
        ans+=1

print(ans)
        
