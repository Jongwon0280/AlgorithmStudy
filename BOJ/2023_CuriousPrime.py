import sys
sys.setrecursionlimit(10000)
input =sys.stdin.readline

def isPrime(num):
    for i in range(2,int(num/2+1)):
        
        if num%i==0:
            return False
        
        
    return True

def dfs(cur,f):
    if f==N:
        print(cur)
    else :
        

        for i in range(1,10):
            if i % 2 ==0:
                continue
            
            
            if isPrime(cur*10+i):
                dfs(cur*10+i,f+1)
            
    
N=int(input())
ls = [2,3,5,7]
for i in ls:
    dfs(i,1)
