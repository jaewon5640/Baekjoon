def solution(myStr):
    answer=list(filter(lambda x:len(x)>0,myStr.translate(str.maketrans('bc','aa')).split('a')))
    return answer if len(answer) else ["EMPTY"]