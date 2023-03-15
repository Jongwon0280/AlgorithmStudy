s,p=map(int,input().split())
dna=list((input()))
check = list(map(int,input().split()))
index=[0]*4
cnt=0
result=0
def add_ck(s):
    global cnt , check,result,index
    if s=='A':
        index[0]+=1
        if index[0]==check[0]:
            cnt+=1
    elif s=='C':
        index[1]+=1
        if index[1]==check[1]:
            cnt+=1
    elif s=='G':
        index[2]+=1
        if index[2]==check[2]:
            cnt+=1
    elif s=='T':
        index[3]+=1
        if index[3]==check[3]:
            cnt+=1

def remove_ck(s):
    global cnt , check,result,index
    if s=='A':
        
        if index[0]==check[0]:
            cnt-=1
        index[0]-=1
    elif s=='C':
        
        if index[1]==check[1]:
            cnt-=1
        index[1]-=1
    elif s=='G':
        
        if index[2]==check[2]:
            cnt-=1
        index[2]-=1
    elif s=='T':
        
        if index[3]==check[3]:
            cnt-=1
        index[3]-=1
for i in check:
    if i == 0:
        cnt+=1

for i in range(p) :
    add_ck(dna[i])
if cnt == 4:
    result+=1
# i는 추가 j는 삭제
for i in range(p,s):
    j=i-p
    add_ck(dna[i])
    remove_ck(dna[j])
    if cnt==4:
        result+=1
print(result)
