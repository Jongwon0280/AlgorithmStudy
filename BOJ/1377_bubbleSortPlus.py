import sys
input = sys.stdin.readline
n = int(input())
ls=[]

for i in range(n):
    ls.append((int(input()),i))

max=0
sort_ls=sorted(ls)


for i in range(n):
    if max < sort_ls[i][1]-i :
        max=sort_ls[i][1]-i
    
print(max+1)
