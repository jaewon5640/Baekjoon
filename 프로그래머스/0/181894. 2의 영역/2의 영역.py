def solution(arr):
    s=-1
    e=-1
    search=len(arr)//2+1 if len(arr)&2 else len(arr)
    for idx in range(search):
        if e==-1 and arr[len(arr)-1-idx]==2:
            e=len(arr)-1-idx
        if s==-1 and arr[idx]==2:
            s=idx
        if e!=-1 and s!=-1:
            break
    if s==-1 and e==-1:
        return [-1]
    else:
        return arr[s:e+1]
        
        
        