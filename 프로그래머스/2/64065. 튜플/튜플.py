def solution(s):
    s = s[1:-1]
    
    # strip(): 문자열 양 끝에 특정 문자 제거
    # split(): ,를 기준으로 문자열을 tokenization 해 iterable 객체 생성
    # map(int, iterable 객체): 각 요소에 대해 int 함수 적용
    s_tuple = [list(map(int, item.strip("{}").split(","))) for item in s.split("},")]

    sorted_s_tuple = sorted(s_tuple, key = len)
    answer = []
    
    for item in sorted_s_tuple:
        element = set(answer)
        answer.append(*(set(item) - element))
    
    return answer