import sys
input = sys.stdin.readline
sum=0
ls=list(map(str,input().split('-')))
if len(ls) ==1:
    
    tmp=str(ls[0].strip()).split('+')
    t=0
    for val in tmp:
        sum+=int(val)
        
    
else :
    
 

    for k in range(len(ls)) :
        
        tmp=str(ls[k].strip()).split('+')
        t=0
        for val in tmp:
            t+=int(val)
            
        
        if k ==0:
            sum+=t
        
        else :
            sum-=t
        
            
        
print(sum)

