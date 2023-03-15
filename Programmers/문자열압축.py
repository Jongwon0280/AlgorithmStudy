def solution(s):
    results=[]
    comp = ''
    cnt=0
    length=len(s)
    if length ==1 :
        return 1
    for i in range(1,(length//2)+1):
        info=''
        comp = s[:i]
        cnt=1
        
        for j in range(i,length,i):  # 0~length-1 unit(1,2, ...)
            if(comp == s[j:i+j]):
                cnt+=1
            else:
                if(cnt!=1):
                    info = info+str(cnt)+comp
                else:
                    info = info+comp
                comp = s[j:j+i]
                cnt=1
       
        if(cnt!=1):
                info = info+str(cnt)+comp
        else:
                info = info+comp
        results.append(len(info))  
                    
            
        
        
    answer=min(results)
    
    return answer
