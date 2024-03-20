def solution(s):
    parentheses = [0]
    
    for item in s:
        if item == '(':
            parentheses.append(item)
        elif item == ')':
            if parentheses[-1]:
                parentheses.pop()
            else: 
                return False
        
    return False if len(parentheses) > 1 else True