
def solution(phone_book):
    answer = True
    prefix = {}
    for i in phone_book:
        prefix[i]=1
    for i in phone_book: #접두사.
        temp = ''
            
        for num in i  :
            
            temp+=num
            if (temp in prefix) & (temp != i):
                return False
                    
        
    return True



