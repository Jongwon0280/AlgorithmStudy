import sys
input = sys.stdin.readline
answer=[]
n = int(input())
for i in range(n):
    
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

    answer.append((int((a/small))*int((b/small))*small))
    
for i in answer :
    print(i)
