def solution(numbers, n):
    answer = 0
    
    for number in numbers:
        if answer+number > n:
            return answer+number
        else: 
            answer += number