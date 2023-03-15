from collections import deque
def solution(number, k):
    
    num_dq = deque(number)

    res = [num_dq.popleft()]

    while num_dq :
        val = num_dq.popleft()
        while res and res[-1]<val and k!=0 :
            res.pop()
            k-=1
        res.append(val)
    
    res=res[0:len(number)-k]
    return ''.join(res)


    
    
