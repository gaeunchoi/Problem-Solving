def solution(arr):
    stk = []   # 빈 리스트 생성
    i = 0   # 초기식
    while i < len(arr) :          
        if not stk :              
            stk.append(arr[i])
            i += 1
        else :
            if stk[-1] < arr[i] :  
                stk.append(arr[i])
                i += 1
            else :
                stk.remove(stk[-1])
    return stk