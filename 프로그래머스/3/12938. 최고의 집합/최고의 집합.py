import math

def solution(n, s):
    answer = []
    best_set = [0]
    a = 0
    # 각 원소를 더할 때 그 중에서 가장 큰 값은 ceil(s/n)
    for divSize in range(n):
        a += best_set[-1]
        best_set.append(math.ceil((s - a)/ (n - divSize)))
    
    index = len(best_set) - 1
    
    while index > 0:
        answer.append(best_set[index])
        index -= 1
    
    if answer[0] < 1:
        return [-1]
    else:
        return answer
