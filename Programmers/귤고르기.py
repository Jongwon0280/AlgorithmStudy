from collections import defaultdict
def solution(k, tangerine):
    
    
    sum=0
    cnt=0
    tang = tangerine
    tang_dic=defaultdict(int)
    length = len(tang)

    for i in range(length):
        tang_dic[tang[i]]+=1
    
    tang_dic = dict(sorted(tang_dic.items(), key=lambda x: x[1],reverse=True))
   

    for i in list(tang_dic.values()):
        if((sum+i)>=k):
            cnt+=1
            break
        else :
            cnt+=1
            sum+=i
    return cnt
    
