import heapq
from heapq import heappush, heappop
def solution(jobs):
    
    jobs=sorted(jobs,key=lambda x :   (x[0],x[1]))


    answer=0
    length = len(jobs)
    q=[]
    s,e =-1,0

    while len(jobs)!=0:
        tmp =[]
        for job in jobs :
            if s<job[0]<=e :
                heappush(q,[job[1],job[0]])
    
        if q :
            item=heappop(q)
        
            jobs.remove([item[1],item[0]])
            s=e
            e+=item[0]
            answer += (e-item[1])
        else :
            item=jobs.pop(0)
            
            s= item[0]-1 # 똑같은 시작시간이 또 존재할 수 있기때문에
            # 반례 [[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]
            e = s+item[1]+1
            answer += (e-item[0])
    return int(answer/length)
    
