def solution(storey):
    a=storey
    length=len(str(a))
    num=list(str(a))
    cnt =0
    up=0
    for i in range(length-1,-1,-1):
        comp = int(num[i]) +up
        up=0
        
        if(comp>5):
            cnt=cnt+(10-comp)
            up=1
        
        elif(comp<5):
            cnt=cnt+comp
        else:
            if(i-1!=-1):
            
                if(int(num[i-1])>=5):
                    up=1
                else:
                    up=0
            cnt=cnt+5

    if(up==1):
        cnt=cnt+1
    return cnt
   
