def solution(k, tangerine):
    tangerineSizeCount = {}
    # 귤 크기별 개수 찾기
    for item in tangerine:
        tangerineSizeCount[item] = tangerineSizeCount.get(item, 0) + 1
    
    tangerineSizeCountValues = list(tangerineSizeCount.values())
    tangerineSizeCountValues.sort(reverse = True)   # 정렬해야 서로 다른 종류의 수의 최솟값 보장

    # 더해서 k값이 되는 수 찾기
    start, end, _sum = 0, 0, 0
    while end <= len(tangerineSizeCountValues):
        if _sum >= k:
            return end - start
        
        elif _sum > k:
            _sum -= tangerineSizeCountValues[start]
            start += 1
        
        else:
            _sum += tangerineSizeCountValues[end]
            end += 1
    
    
