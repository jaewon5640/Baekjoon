msg=input().upper().rstrip()
strSet=set(msg)
result=''
maxValue=0
maxCount=0
for s in strSet:
    sCnt=msg.count(s)
    if sCnt>maxValue:
        maxCount=0
        result=s
        maxValue=sCnt
    elif sCnt==maxValue:
        maxCount+=1
if maxCount > 0:
    print('?')
else:
    print(result)