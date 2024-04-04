import math
def solution(n,a,b):
    answer = 1
    if a > b:
        a, b = b, a
    while True:
        if math.ceil(a/2) == math.ceil(b/2):
            break
        a = math.ceil(a/2)
        b = math.ceil(b/2)
        answer += 1
        
    return answer