def solution(num_list):
    answer=0
    while True:
        num_list=list(filter(lambda x:x!=1,num_list))
        if len(num_list)==0:
            break
        num_list=list(map(lambda x:(x-1)//2 if x&1 else x//2,num_list))
        answer+=len(num_list)
    return answer