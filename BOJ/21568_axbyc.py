import sys
input = sys.stdin.readline
def rec(a,b):
    params=[0]*2
    if b==0:
        params[0]=1
        params[1]=0
        return params
        
    q=a//b
    params=rec(b,a%b)
    new_x=params[1]
    new_y=params[0]-params[1]*q
    
    params[0]=new_x
    params[1]=new_y
    return params
    

def GCP(a,b):
    global gcp
    if a< b :
        temp =a
        a=b
        b=temp
    if a%b == 0 :
        gcp = b
    else :
        GCP(b,a%b)
    


a,b,c= map(int,input().split())
GCP(a,b)

if c%gcp!=0:
    print(-1)
else :
    new_c= c//gcp
    qq=rec(a,b)
    print(qq[0]*new_c,qq[1]*new_c)


