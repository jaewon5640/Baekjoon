def solution(strArr):
    return list(filter(lambda x:not 'ad' in x, strArr))
    