n=int(input())
fibo=[0,1,1]
if n < 2:
    print(fibo[n])
else:
    for _ in range(n-2):
        fibo=[fibo[1],fibo[2],fibo[1]+fibo[2]]
    print(fibo[2])