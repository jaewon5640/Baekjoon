def solution(arr):
    n=range(len(arr))
    for i in n:
        for j in n:
            if arr[i][j]!=arr[j][i]:
                return 0
    return 1
                