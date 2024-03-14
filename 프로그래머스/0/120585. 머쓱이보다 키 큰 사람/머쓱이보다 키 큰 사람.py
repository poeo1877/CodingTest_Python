def solution(array, height):
    array.append(height)
    array.sort()
    answer = []
    for item in array:
        if item > height:
            answer.append(item)

    return len(answer)