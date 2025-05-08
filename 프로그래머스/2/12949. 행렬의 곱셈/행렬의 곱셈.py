import numpy as np
def solution(arr1, arr2):
    numpy1 = np.array(arr1)
    numpy2 = np.array(arr2)
    result = numpy1 @ numpy2
    return result.tolist()