from collections import deque
import copy

def recursive(start,cnt,total,limit,maps,r,answers):
    
    route = []
    if cnt == total:
        
        z=copy.deepcopy(r)
        
        answers +=[z]
        
        return [r]
    if start in maps.keys():  
        for i in range(len(maps[start])):
            if limit[start][i] !=1 :
    
                limit[start][i]=1
                r+=[maps[start][i]]
                [(recursive(maps[start][i],cnt+1,total,limit,maps,r,answers))] 
                limit[start][i]=0
                r.pop()
                
        return answers
def solution(tickets):
    
    total = len(tickets)

    maps = {}


    limit = {}

    for i in tickets :
        if i[0] not in maps.keys():
            maps[i[0]]=[i[1]]
            limit[i[0]]=[0]
        else :
            maps[i[0]]+=[i[1]]
            maps[i[0]]=sorted(maps[i[0]],reverse=True)
            limit[i[0]]+=[0]
    answers =[]


    answers=recursive('ICN',0,total,limit,maps,['ICN'],[])


    return sorted(answers)[0]
    

            
   
