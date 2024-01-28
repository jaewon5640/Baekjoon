def solution(n):
    return [[1 if x==y else 0 for y in range(n)] for x in range(n)]