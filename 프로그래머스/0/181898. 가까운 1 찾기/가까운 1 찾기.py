def solution(arr, idx):
    answer=-1
    for i,num in enumerate(arr[idx:]):
        if num==1:
            answer=i+idx
            break
    return answer
        