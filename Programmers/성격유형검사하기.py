def solution(survey, choices):
    answer =''
    dict1 = [{'R' : 0, 'T' : 0}, {'C' : 0, 'F' : 0},
            {'J' : 0, 'M' : 0},{'A' : 0, 'N' : 0}]
    add = [3,2,1,0,1,2,3]
    length=len(choices)
    k,k1 =0,0
    for index, i in enumerate(survey):
        j=0
        for j in range(0,4,1):
            if(i[1] in list(dict1[j].keys())):
                k=j
                break
        for j in range(0,4,1):
            
                
            if(i[0] in list(dict1[j].keys())):
                
                k1 =j
                break
        
        if(choices[index]>4):
            
            dict1[k][i[1]]+=add[choices[index]-1]
        else:
            
            if(choices[index]<4):
                
                dict1[k1][i[0]]+=add[choices[index]-1]
        
        
    for i in range(0,4,1):
        
    
        if(list(dict1[i].values())[0]<list(dict1[i].values())[1]):
            answer+=list(dict1[i].keys())[1]
        else:
            answer+=list(dict1[i].keys())[0]


    return answer
