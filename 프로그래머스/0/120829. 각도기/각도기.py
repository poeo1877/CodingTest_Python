def solution(angle):
    if angle % 90 <= 0:
        return ( angle // 90 ) * 2
    else:
        return 2 * (angle // 90) + 1
