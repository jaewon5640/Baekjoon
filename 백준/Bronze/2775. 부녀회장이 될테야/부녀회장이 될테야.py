case = int(input())
for x in range(case):
    k = int(input())
    n = int(input())
    arr = [i+1 for i in range(n)]
    tmpArr = [0 for i in range(n)]
    if k == 0:
        print(arr[n-1])
    else:
        for i in range(k):
            for j in range(n):
                tmpArr[j] = sum(arr[:j+1])
            arr = tmpArr[:]
        print(arr[n-1])