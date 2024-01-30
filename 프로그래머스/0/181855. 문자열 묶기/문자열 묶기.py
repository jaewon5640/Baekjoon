def solution(strArr):
    dic={}
    for num in list(map(lambda x:len(x),strArr)):
        if num in dic:
            dic[num]+=1
        else:
            dic[num]=1
    return max(dic.values())