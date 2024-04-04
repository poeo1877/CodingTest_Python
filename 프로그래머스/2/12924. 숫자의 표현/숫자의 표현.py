# x(x+1) = 2n
# 두 개 이상으로 합하려면 n/2 부터 가능
import math

def solution(n):
    
    start, end, count, total = 1,1,1,1
    
    while end != n:
        if total == n:
            count += 1
            end += 1
            total += end
        
        elif total > n:
            total -= start
            start += 1
    
        else:
            end += 1
            total += end
    
    return count
        
    
