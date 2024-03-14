def solution(s):
    tokens = list(map(int, s.split(' ')))
    return " ".join([str(min(tokens)), str(max(tokens))])