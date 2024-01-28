def solution(numLog):
    previous = numLog[0]
    control = {1:"w",-1:"s",10:"d",-10:"a"}
    result = ""
    for num in numLog[1:]:
        result += control[num-previous]
        previous = num
    return result
        