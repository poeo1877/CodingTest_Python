# # 야근 지수를 최소화 하기 위해서는 각 원소가 고르게 작은 값이 되어야 한다.
# def solution(n, works):
    
#     while n > 0:
#         works.sort(reverse = True)
#         if works[0] > 0:
#             works[0] = works[0] - 1
#         else:
#             for index in range(1, len(works)):
#                 if index >= len(works) - 1:
#                     n = 1
#                     break
#                 works[index] = works[index] - 1
                
#         n -= 1
#     return calcOverNightIndex(works)

# # 야근 지수 구하는 함수
# def calcOverNightIndex(arr):
#     OverNightIndex = 0
#     for item in arr:
#         OverNightIndex += item**2
    
#     return OverNightIndex

def solution(n, works):
    answer = 0
    
    worksItemCounter = [0] * (max(works) + 1)
    for i in works:
        worksItemCounter[i] += 1
    
    # 야근 지수 최소값 찾기
    while n > 0:
        if len(worksItemCounter) <= 0:
            break
        
        if len(worksItemCounter) >= 2 and worksItemCounter[-1] > 0:
            worksItemCounter[-1] -= 1
            worksItemCounter[-2] += 1
            n -= 1
        elif len(worksItemCounter) > 0 and worksItemCounter[-1] > 0:
            worksItemCounter[-1] -= 1
            n -= 1
        
        if len(worksItemCounter) > 0 and worksItemCounter[-1] == 0:
            worksItemCounter.pop()
    
    # 야근지수 계산
    for i in range(len(worksItemCounter)):
        answer += worksItemCounter[i]*(i**2)
    
    return answer