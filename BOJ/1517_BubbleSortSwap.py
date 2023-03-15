result = 0
def merge_sort(s,e):
    global result
    global num
    if(s<e):
        mid = int(s+(e-s)/2)
        merge_sort(s,mid)
        merge_sort(mid+1,e)
        for i in range(s,e+1):
            tmp[i]=num[i]
            
        
        
        k=s
        in1 =s
        in2=mid+1
        while in1<=mid and in2 <= e:
            if tmp[in1]>tmp[in2]:
                num[k]=tmp[in2]
                result+=in2-k
                
                k+=1
                in2+=1
                
            else :
                num[k]=tmp[in1]
                k+=1
                in1+=1
        while in1<=mid:
            num[k]=tmp[in1]
            k+=1
            in1+=1
                
        while in2<=e:
            num[k]=tmp[in2]
            k+=1
            in2+=1
    else :
        return

    return result   


n = int(input())

num=list(map(int,input().split()))
tmp = [0]*n
merge_sort(0,n-1)
print(result)
