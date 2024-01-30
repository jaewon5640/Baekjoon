def solution(my_string, queries):
    my_string=list(my_string)
    for s,e in queries:
        sub=my_string[s:e+1]
        sub.reverse()
        my_string=my_string[:s]+sub+my_string[e+1:]
    return "".join(my_string)