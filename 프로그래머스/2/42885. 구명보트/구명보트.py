# def solution(people, limit):
#     #효율성 테스트 실패
#     answer = 0
#     people.sort(reverse = True)
    
#     for person in people:
#         if person > limit - 40:
#             answer += 1 
#             continue
#         secondEscapeeIndex = 0
#         # 2명 짝 지을 수 있는지 탐색
#         for index in range(1, len(people)//2+1):
#             if (people[-index] + person) <= limit:
#                 secondEscapeeIndex = index
#             else:
#                 break
        
#         # 2명 짝 지어 나갈 수 있는가?
#         if secondEscapeeIndex > 0:
#             people.pop(-secondEscapeeIndex)
        
#         answer += 1
    
#     return answer

def solution(people, limit):
    answer = 0
    people.sort()  # 오름차순 정렬
    left, right = 0, len(people) - 1  # 투 포인터 초기화

    while left <= right:
        # 가장 가벼운 사람과 가장 무거운 사람의 무게 합이 제한 이하인 경우
        if people[left] + people[right] <= limit:
            left += 1  # 가장 가벼운 사람을 보트에 태움
        # 무거운 사람은 항상 보트에 태움
        right -= 1
        answer += 1  # 보트 개수 증가

    return answer
