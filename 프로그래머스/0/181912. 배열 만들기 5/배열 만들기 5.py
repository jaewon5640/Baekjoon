def solution(intStrs, k, s, l):
    answer=[]
    for str in intStrs:
        num=int(str[s:s+l])
        if num>k:
            answer.append(num)
    return answer