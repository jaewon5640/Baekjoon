def solution(myString, pat):
    result=0
    s=0
    while s+len(pat)<=len(myString):
        if pat==myString[s:s+len(pat)]:
            result+=1
        s+=1
    return result