import heapq
from heapq import heappush, heappop
def solution(operations):
    answer = [0,0]
    q=[]


    for op in operations:
        tmp=op.split()
        if tmp[0]=='I' :
            heappush(q,int(tmp[1]))
        if q :
            
            if (tmp[0] == 'D') & (tmp[1]=='-1') :
                
                heappop(q)
        if (tmp[0] == 'D') & (tmp[1]=='1') :
            q = heapq.nlargest(len(q), q)[1:]
            heapq.heapify(q)   
    if(q):
        
        a=sorted(list(q))

        a=[a[len(a)-1],a[0]]
        return a

    
    return answer
