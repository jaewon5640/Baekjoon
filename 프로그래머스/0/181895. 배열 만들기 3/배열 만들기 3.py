def solution(arr, intervals):
    result=[]
    for s,e in intervals:
        result.extend(arr[s:e+1])
    return result