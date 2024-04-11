import math
def solution(n, left, right):
    matrix = []    
    for col in range(left//n, right//n+1):
        for row in range(1, n+1):
            matrix.append(max(row, col+1))
    answer = matrix[left%n : -(n-1-right%n)] if n-1-right%n > 0 else matrix[left%n:]
    # list comprehension으로 2차원 n by n 배열 생성 및 값 초기화
    
    # 첫번째 행 더하기
#     answer += [*matrix[left//n][left%n:]]
    
#     for i in range(left//n + 1, right//n):
#         answer += [*matrix[i][:]]
#     # 마지막 행 더하기
#     if right/(n-1) - right//(n-1) > 0:
#         answer += [*matrix[right//n][:right%n+1]]
    
    # ## 시간초과
    # # 2차원 배열을 1차원으로 만들기
    # arr = [matrix[i][j] for i in range(n) for j in range(n)]
    # return arr[left:right+1]
    
    return answer