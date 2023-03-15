import sys
input = sys.stdin.readline

n = int(input())
num = [0]*10001
for i in range(n):
    inp = int(input())
    num[inp]+=1

for i in range(len(num)):
    if num[i]>0:
        for j in range(num[i]):
            print(i)
    
