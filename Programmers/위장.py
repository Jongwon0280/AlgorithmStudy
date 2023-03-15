
def solution(clothes):
    cloth = {}
    
    for i in clothes :
        b=i[1]
        if b in list(cloth.keys()):
            cloth[b]+=1
            
        else:
            cloth[b] =1 
    
    k = list(cloth.keys()) # 옷별 가짓수
    sum=1
    for i in k:
        sum*=(cloth[i]+1)
        
    sum=sum-1
        
        
    return sum
