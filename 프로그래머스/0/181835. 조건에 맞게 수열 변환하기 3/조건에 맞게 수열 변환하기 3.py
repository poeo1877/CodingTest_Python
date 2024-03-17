def solution(arr, k):
    if k%2:
        arr = [num*k for num in arr]
    else:
        arr = [num+k for num in arr]
    return arr