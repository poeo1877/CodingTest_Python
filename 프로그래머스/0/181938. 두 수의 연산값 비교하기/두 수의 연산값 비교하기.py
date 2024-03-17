def solution(a, b):
    if int(''.join([str(a), str(b)])) > 2*a*b:
        return int(''.join([str(a), str(b)]))
    else:
        return 2*a*b