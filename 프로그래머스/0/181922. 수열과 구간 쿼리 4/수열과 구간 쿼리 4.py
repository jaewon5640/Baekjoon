def solution(arr, queries):
    for s,e,k in queries:
        arr = [num+1 if (s<=idx<=e) and (idx==0 or idx%k==0) else num for idx,num in enumerate(arr)]
    return arr