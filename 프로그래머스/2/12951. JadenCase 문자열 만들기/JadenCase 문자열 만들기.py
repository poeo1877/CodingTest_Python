def solution(s):
    tokens = s.split(' ')
    
    answer = []
    for token in tokens:
        if token:
            token = token.lower()
            jadenCase = token[0].upper() + token[1:]
            answer.append(jadenCase)
        else: 
            answer.append(token)

    answer = " ".join(answer)
    return answer