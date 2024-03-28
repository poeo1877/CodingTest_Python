def solution(n):
    odd = 1                 #홀수 index 값
    even = 0                #짝수 index 값
    for index in range(1, n+1):
        if index % 2 == 0:
            even += odd
        else: 
            odd += even
        
    return max(even, odd) % 1234567
