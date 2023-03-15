def solution(s):
    answer = True
    b=list(s) # '(' , ')' ....

    space=0

    for i in b:
        
        if i == '(' :
            space+=1
        if (i == ')' )&(space!=0) :
            space-=1
        elif (i == ')' )&(space==0) :
            return False
    if space == 0 :
        return True
    else :
        return False
   

