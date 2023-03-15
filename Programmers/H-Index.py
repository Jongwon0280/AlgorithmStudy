def solution(citations):
    answer = 0
    c=sorted(citations)
    if max(c) ==0:
        return 0
    h=len(c)
    for i in range(len(c)):
        h=len(c)-i
        if c[i]>=h :
            return h
         
    
