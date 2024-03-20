def solution(s):
    funcCount = 0
    removedZero = 0
    
    while(s != "1"):
        zeroCounter = s.count('0')
        s = s.replace('0', '')
        funcCount += 1

        if zeroCounter > 0:
            removedZero += zeroCounter

        s = "".join(bin(len(s)))[2:]
    
    return [funcCount, removedZero]

