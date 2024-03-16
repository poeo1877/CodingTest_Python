def solution(dot):
    if dot[1] > 0:
        if dot[0] >0:
            return 1
        else: 
            return 2
    elif dot[0] > 0:
        return 4
    else:
        return 3
