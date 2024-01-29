def solution(l, r):
    answer=[]
    num=1
    value=5
    while True:
        if r<value: break
        value=int(str(bin(num))[2:].replace('1','5'))
        if l<=value<=r: answer.append(value)
        num+=1
    return [-1] if len(answer)==0 else sorted(answer)