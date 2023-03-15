st = input()
ls =[]
answer=""
for s in st :
    ls.append((-1*int(s),int(s)))
ls=sorted(ls)

for i in ls:
    answer+=str(i[1])
print(answer)
