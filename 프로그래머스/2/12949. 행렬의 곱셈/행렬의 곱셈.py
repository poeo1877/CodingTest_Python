import numpy as np

def solution(arr1, arr2):
    _arr1 = np.array(arr1)
    _arr2 = np.array(arr2)
    
    result = np.dot(_arr1, _arr2)
    result = result.tolist()
    
    return result