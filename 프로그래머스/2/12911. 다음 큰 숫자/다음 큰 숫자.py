def solution(n):
    nOneCount = bin(n)[2:].count('1')
    
    while True:
        n += 1
        oneCount = bin(n)[2:].count('1')
        if nOneCount == oneCount:
            return n        
        
