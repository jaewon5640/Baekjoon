T=int(input())
for _ in range(T):
    result=""
    cnt,msg=input().split()
    for val in msg:
        result+=val*int(cnt)
    print(result)