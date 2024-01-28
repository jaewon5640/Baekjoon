def solution(a, d, included):
    result = 0
    arr=[x for x in range(a,a+d*len(included),d)]
    for key,value in dict(zip(arr,included)).items():
        if value: result += key
    return result