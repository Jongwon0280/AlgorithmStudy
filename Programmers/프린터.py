from collections import deque
def solution(priorities, location):
    
    
    dic = []
    value =[]

    
    for i in range(0,len(priorities)) :
        dic.append( [i,priorities[i]])
    queue=deque(dic)


    while len(queue) !=0:
        item=queue.popleft()
    
        if(item[1] == max(priorities)):
            value.append(item)
            priorities[priorities.index(max(priorities))]=0
        
        else :
            queue.append(item)
    return (list(dict(value).keys()).index(location))+1

# keys_자료형 [2, 3, 0, 1] -> 2번이 위치하는 인덱스값인 0출력해주는데

# +1 1번째로 나왔다.
