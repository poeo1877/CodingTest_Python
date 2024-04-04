def solution(n):
    odd, even = 1, 2
    
    for number in range(1, n):
        if number % 2 == 0:
            even += odd
        else: 
            odd += even
    return even % 1234567 if n % 2 == 0 else odd % 1234567