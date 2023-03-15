from collections import deque
def solution(prices):


    answers =[]
    prices=deque(prices)

    while prices : # n * (n-1) -> n
        item=prices.popleft()
        cnt = 0
        for price in prices:
            if price >= item :
                cnt+=1
            else :
                cnt+=1
                break
        answers.append(cnt)
    return answers
    
