def solution(s):
    answer = 0
    
    for num in range(len(s)):
        _s = s[num:] + s[:num] 
        answer += isValidParenthesis(_s, num)
    
    return answer

def isValidParenthesis(s, x):
    pattern = {
        '[': ']', 
        '(': ')', 
        '{': '}'
    }
    
    stack = []
    for char in s:
        stack.append(char)
        if len(stack) >= 2 and (stack[-2] in pattern and stack[-1] == pattern[stack[-2]]):
            stack.pop()
            stack.pop()
    return 1 if not stack else 0 
    
