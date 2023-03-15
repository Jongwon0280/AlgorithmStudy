def solution(bridge_length, weight, truck_weights):
    
    from collections import deque
    
    queue = deque([0]*bridge_length)
    total =0
    times =0

    while truck_weights :
        times+=1
    
        item=queue.popleft()
    
        total -= item
    
        if total + truck_weights[0] > weight :
            queue.append(0)
        else :
            tmp=truck_weights.pop(0)
            total += tmp
            queue.append(tmp)
    return (times + bridge_length)
