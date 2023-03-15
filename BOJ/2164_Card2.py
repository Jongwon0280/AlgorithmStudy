from collections import deque
n = int(input())
card=deque([])
for i in range(n,0,-1):
    card.append(i)

while card:
    if(len(card)!=1):
        
        card.pop()
        t=card.pop()
        card.appendleft(t)
    else :
        print(card.pop())
        break
