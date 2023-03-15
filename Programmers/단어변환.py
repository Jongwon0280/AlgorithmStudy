from collections import deque
def func1(item,words):
    w = []
    for i in words :
        cnt=0
        for j in range(len(item[0])) :
            if item[0][j] != i[j]:
                
                cnt+=1
        if cnt==1:
            w.append(i)
    return w
def solution(begin, target, words):

    cnt =0

    queue=[]
    queue = deque(queue)
    queue.append([begin,0])

    while queue :
        item = queue.popleft()
    
        add=func1(item,words)
        for i in add :
            if(i == target):
                return (item[1]+1)
            
        
            queue.append([i,item[1]+1])
            words.remove(i)
    return 0
