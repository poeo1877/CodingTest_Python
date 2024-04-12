def solution(citations):
    n = len(citations)
    citations.sort(reverse=True)

    left = 0
    right = n - 1
    # 이진 검색을 사용하여 H-Index를 찾는다
    while left <= right:
        mid = (left + right) // 2
    # citations[mid] >= mid + 1 조건을 만족하는 경우
        if citations[mid] >= mid + 1:
            left = mid + 1
        else:
            right = mid - 1
      # left는 H-Index 값을 가리킨다
    return left

