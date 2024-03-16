def solution(sides):
    biggestEdge = max(sides)
    sides.remove(biggestEdge)
    return 1 if sum(sides) > biggestEdge else 2