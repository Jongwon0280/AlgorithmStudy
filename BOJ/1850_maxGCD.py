import sys
input = sys.stdin.readline

a,b = map(int,input().split())

if b>a:
    large = b
    small=a
else :
    large =a
    small=b
while large % small!=0 :
    
    temp=large % small
    if temp>small:
        large = temp
    else :
        large = small
        small = temp

print('1'*small)
