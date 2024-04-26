def solution(clothes):
    # 인자를 dictionary 형태로 변환
    dic_clothes = {}    
    for cloth, _type in clothes:
        if _type in dic_clothes:
            dic_clothes[_type].append(cloth)
        else:
            dic_clothes[_type] = [cloth]
    answer = 1
    # 옷 종류별 개수 세기
    clothes_count = []
    for item in dic_clothes:
        clothes_count.append(len(dic_clothes[item]))    
    
    # 각 종류별 경우의 수는 원소의 개수 + 그 종류의 옷을 아예 안 입는 경우(= 1)
    for number in clothes_count:
        answer *= (number+1)
    
    # 옷을 하나도 입지 않는 경우를 제외
    return answer-1