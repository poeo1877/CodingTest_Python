def solution(n):
    for i in range(1, n):
        if i*i == n:
            return 1
        if i*i > n:
            return 2
