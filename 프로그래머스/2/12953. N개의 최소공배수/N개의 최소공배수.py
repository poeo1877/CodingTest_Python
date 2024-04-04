import math
# math에 lcm() 없다. gcd()도 인자 2개만 받는다.
def solution(arr):
    lcmValue = 1
    for number in arr:
        lcmValue = lcm(lcmValue, number)
    
    return lcmValue

def lcm(a, b):
    return a * b // math.gcd(a, b)
