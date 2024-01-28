def solution(arr, flag):
    answer=[]
    for num,b in zip(arr,flag):
        if b:
            answer.extend([num]*num*2)
        else:
            answer=answer[:len(answer)-num]
    return answer