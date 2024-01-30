def solution(arr):
    i=0
    num=0
    while True:
        if len(arr) <= 2**i:
            num=2**i-len(arr)
            break
        i+=1
    return arr+[0]*num