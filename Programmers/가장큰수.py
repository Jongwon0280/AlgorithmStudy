def solution(numbers):
    numbers=[str(x) for x in numbers]

    numbers.sort(key=lambda x : 3*x ,reverse=True)
    
    answers = str(int(''.join(numbers)))
    return answers
    
    
