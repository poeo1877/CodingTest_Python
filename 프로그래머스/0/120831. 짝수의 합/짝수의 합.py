def solution(n):
    if (n % 2 != 0):
        n = n-1        
    if n < 0:
        return 0
    return (n + solution(n-2))
