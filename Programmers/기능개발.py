import math
def solution(progresses, speeds):
    
    rest_work=[]

    for index,i in zip(range(0,len(progresses),1),progresses):
        a=int(math.ceil((100-i)/speeds[index]))
        rest_work.append(a)

    count = []
    cnt=0
    out =0
    for i in range(0,len(rest_work),1) : #기능개수만큼 루프를 돈다.
        if(rest_work[i]!=0): # 
            cnt+=1
            val = rest_work[i]
            rest_work[i]=0
            out+=1
            for j in range(i+1,len(rest_work),1):
                if ((rest_work[j]-val<=0) | (rest_work[j]==0)) & (out==j):
                    rest_work[j]=0
                    out+=1
                    cnt+=1
                else :
                    if(rest_work[j]-val<0):
                        rest_work[j]=0
                    else :
                        rest_work[j]-=val
                
        
            count.append(cnt)
            cnt=0
        else :
            pass

    return count
    
    


    
