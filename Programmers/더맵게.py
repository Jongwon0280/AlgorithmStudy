import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    cnt=0
    a,b=0,0
    
    while (scoville[0]<K) & (len(scoville)!=1):
        
        a=heapq.heappop(scoville)
        b=heapq.heappop(scoville) * 2
        heapq.heappush(scoville,a+b)
        cnt+=1
    if a+b < K :
        return -1
    else :
        return cnt
    
    


