import numpy as np
# 머신러닝 과목 공부하며 사용하였으나, 실제 코딩테스트에서는 해당 라이브러리
# 사용할 수 없는 경우가 있다. 다른 방법으로 이 문제를 해결하는 것이 바람직하다.
def solution(arr1, arr2):
    _arr1 = np.array(arr1)
    _arr2 = np.array(arr2)
    
    result = np.dot(_arr1, _arr2)
    result = result.tolist()
    
    return result