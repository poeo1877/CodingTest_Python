def solution(arr, n):
    answer = []
    if len(arr) % 2:
        return [item + n if not index % 2 else item for index, item in enumerate(arr)]
    else:
        return [item + n if index % 2 else item for index, item in enumerate(arr)]
