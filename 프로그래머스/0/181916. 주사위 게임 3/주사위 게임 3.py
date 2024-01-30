def solution(a, b, c, d):
    dic={}
    for i in [a,b,c,d]:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    arr=sorted(dic.items(),key=lambda x:x[1],reverse=True)
    if len(arr)==1:
        return arr[0][0]*1111
    elif len(arr)==2:
        if arr[0][1]==3:
            return (10*arr[0][0]+arr[1][0])**2
        else:
            return (arr[0][0]+arr[1][0])*abs(arr[0][0]-arr[1][0])
    elif len(arr)==3:
        return arr[1][0]*arr[2][0]
    else:
        return min(arr[0][0],arr[1][0],arr[2][0],arr[3][0])
    
        