import itertools
def solution(numbers):
    answer = 0
    value=[]
    cc =[]
    numbers=list(numbers)
    for i in range(len(numbers)):
        numbers[i]= int(numbers[i])

    for i in range(0,len(numbers)):
        n=itertools.permutations(numbers,i+1)
        n=list(n)
    
        for j in range(len(n)):
            s=''
            for k in range(0,len(n[j])):
                s+=str(n[j][k])
            
            value.append(int(s))  
    value=list(set(value))
    ck = 0  
    for i in value :
        ck=0
        if (i != 1) & (i!=0) :
            j=2
            while (j * j) <=i :
                if(i%(j)==0):
                    ck=1
                    break
            
                j+=1
            if ck == 0:
                cc.append(i)
    return len(cc)
