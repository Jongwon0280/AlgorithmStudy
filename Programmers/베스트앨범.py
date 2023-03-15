

def solution(genres, plays):
    
    answer=[]
    chart ={}
    genres_sum ={}
    for i in range(len(genres)):
        
        if genres[i] not in chart.keys():
            chart[genres[i]]= [(plays[i],i)]
            genres_sum[genres[i]]= plays[i]
        else :
            chart[genres[i]]+= [(plays[i],i)]
            genres_sum[genres[i]]+= plays[i]
            
    
    genres_sum=sorted(genres_sum.items(),key=lambda x : x[1],reverse=True)
    
    for key in genres_sum:
        genre = chart[key[0]]
        genre = sorted(genre,key = lambda x : (-x[0],x[1]))
        
        for i in range(len(genre)):
            if i==2:
                
                break
            answer.append(genre[i][1])
            
    return answer     

 
