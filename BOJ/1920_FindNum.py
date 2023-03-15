import sys
input=sys.stdin.readline
n = int(input())
ls =[]
find =[]
ls= list(map(int,input().split()))

f = int(input())

find= list(map(int,input().split()))

ls.sort()

left =0
right = len(ls)-1

for key in find:
    sig = 0
    left =0
    right=len(ls)-1

    while left<=right:
        mid = int((left+right)/2)
        if ls[mid]==key:
            sig=1
            break
        elif ls[mid]>key:
            right = mid-1
        else :
            left = mid+1
        
    if sig:
        print(1)
    else :
        print(0)
    
    
