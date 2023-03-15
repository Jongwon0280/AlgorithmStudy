n = int(input())
stk = []
ans=[-1]*n
num = list(map(int,input().split()))
for i in range(n):
    while stk and num[stk[-1]]<num[i]:
        ans[stk.pop()]=num[i]
    
    stk.append(i)

print(*ans)
