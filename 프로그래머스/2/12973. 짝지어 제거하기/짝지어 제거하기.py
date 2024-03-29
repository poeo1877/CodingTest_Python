def solution(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:     #조건문 항 순서 중요
            stack.pop()
        else:
            stack.append(char)
    return 1 if not stack else 0        #empty stack == 짝지어 제거 성공
