def solution(rny_string):
    return ''.join(['rn' if char == 'm' else char for char in rny_string])