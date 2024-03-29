import math
# 정사각형의 한 변의 길이 == root 씌운 yellow
def solution(brown, yellow):
    for i in range(1, int(math.sqrt(yellow))+1):
        # yellow의 약수 찾아 사각형 가로, 세로 찾기
        if yellow % i == 0:
            width = yellow // i
            height = i
            # yellow area를 감싸는 brown 개수 찾기
            if (2 * width) + (2 * height) + 4 == brown:
                return [width + 2, height + 2]
